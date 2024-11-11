import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)        
        extracted_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()  # Append the text from each page
        
        return extracted_text
def input_pdf():
    pdf_path = input("Please enter the path to the PDF file: ")
    extracted_text = extract_text_from_pdf(pdf_path)

    #print("Extracted text from the PDF:")
    #print(extracted_text)
    return extracted_text
