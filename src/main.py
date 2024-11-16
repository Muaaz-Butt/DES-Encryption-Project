from master_key_generator import generate_master_key
from initial_permutation import initial_permutation
from split_key import split_key_into_32_bits
from key_scheduling import DESKeyScheduler
from text_handling import text_to_binary, pad_binary, divide_into_blocks
from take_input_pdf import input_pdf
from des_cipher import DESCipher
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import datetime

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
    
    # Create styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    content_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        leading=14
    )
    
    # Create the PDF content
    elements = []
    
    # Add timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(f"Generated on: {timestamp}", styles['Normal']))
    elements.append(Spacer(1, 0.2 * inch))
    
    # Add title
    elements.append(Paragraph(title, title_style))
    
    # Add content
    # Split content into manageable chunks to avoid overflow
    chunk_size = 5000  # Adjust this value based on your needs
    for i in range(0, len(content), chunk_size):
        chunk = content[i:i + chunk_size]
        elements.append(Paragraph(chunk, content_style))
        elements.append(Spacer(1, 0.2 * inch))
    
    # Build the PDF
    doc.build(elements)

def main():
    try:
        print("Reading PDF file...")
        plaintext = input_pdf()
        print(f"Successfully extracted text ({len(plaintext)} characters)")
        
        name = "MUAAZBUT"
        master_key = generate_master_key(name)
        print("Master key generated successfully")
        
        # Create DES cipher instance
        des = DESCipher(master_key)
        
        # Encrypt the text
        print("\nEncrypting text...")
        ciphertext = des.encrypt(plaintext)
        print("Encryption successful!")
        print(f"\nFirst 64 bits of ciphertext: {ciphertext[:64]}")
        
        # Decrypt the text
        print("\nDecrypting text...")
        decrypted_text = des.decrypt(ciphertext)
        print("Decryption successful!")
        
        # Verify results
        if decrypted_text == plaintext:
            print("\nVerification successful: Decrypted text matches original!")
        else:
            print("\nWarning: Decrypted text differs from original!")
            
        # Save results to PDF files
        print("\nGenerating PDF files...")
        
        # Create encrypted PDF
        create_pdf_document(
            "encrypted.pdf",
            "DES Encrypted Text",
            ciphertext
        )
        
        # Create decrypted PDF
        create_pdf_document(
            "decrypted.pdf",
            "DES Decrypted Text",
            decrypted_text
        )
            
        print("\nResults have been saved to 'encrypted.pdf' and 'decrypted.pdf'")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()