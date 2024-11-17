import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file with error handling."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            if len(pdf_reader.pages) == 0:
                raise ValueError("PDF file is empty")
                
            extracted_text = ""
            for page_num in range(len(pdf_reader.pages)):
                try:
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    # Remove non-printable characters
                    if page_text:
                        page_text = ''.join(char for char in page_text if char.isprintable())
                        extracted_text += page_text
                except Exception as e:
                    print(f"Warning: Error extracting text from page {page_num + 1}: {str(e)}")
                    continue
                    
            if not extracted_text:
                raise ValueError("No text could be extracted from the PDF")
                
            return extracted_text
            
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error processing PDF: {str(e)}")
