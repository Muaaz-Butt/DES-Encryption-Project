import tkinter as tk
from tkinter import filedialog, messagebox
from master_key_generator import generate_master_key
from take_input_pdf import extract_text_from_pdf
from des_cipher import DESCipher
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime
import os

def create_pdf_document(filename, title, content):
    """Create a PDF document with given title and content."""
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, alignment=1)
    content_style = ParagraphStyle('ContentStyle', parent=styles['Normal'], fontSize=12)

    elements = [Paragraph(f"Generated on: {datetime.datetime.now()}", styles['Normal'])]
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 24))
    elements.append(Paragraph(content, content_style))
    doc.build(elements)

class DESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Encryption & Decryption with DES")
        self.root.geometry("500x300")
        
        # Path to the selected file
        self.file_path = tk.StringVar()
        
        # GUI Elements
        tk.Label(root, text="Select a PDF file", font=("Arial", 14)).pack(pady=10)
        tk.Entry(root, textvariable=self.file_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_file).pack(pady=5)
        
        # Button to perform both encrypt and decrypt actions on the selected PDF
        tk.Button(root, text="Encrypt & Decrypt PDF", command=self.encrypt_and_decrypt_pdf, bg="lightgreen").pack(pady=20)
    
    def browse_file(self):
        """Open file dialog to select a PDF file."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.file_path.set(file_path)
    
    def encrypt_and_decrypt_pdf(self):
        """Encrypt and decrypt the selected PDF file on a single click."""
        file_path = self.file_path.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid PDF file")
            return
        
        try:
            # Extract text from the selected PDF file
            plaintext = extract_text_from_pdf(file_path)
            if not plaintext:
                raise ValueError("Failed to extract text from PDF")

            # Generate master key and encrypt the text
            name = "MUAAZBUT"
            master_key = generate_master_key(name)
            des = DESCipher(master_key)

            ciphertext = des.encrypt(plaintext)
            create_pdf_document("encrypted.pdf", "DES Encrypted Text", ciphertext)
            
            # Decrypt the ciphertext
            decrypted_text = des.decrypt(ciphertext)
            create_pdf_document("decrypted.pdf", "DES Decrypted Text", decrypted_text)

            messagebox.showinfo("Success", "PDF encrypted and decrypted. Files saved as 'encrypted.pdf' and 'decrypted.pdf'")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = DESApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
