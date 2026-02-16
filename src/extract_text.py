import pdfplumber
import json

def extract_text_from_pdf(pdf_path):
    extracted_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            extracted_data.append({
                "page_number": i + 1,
                "content": text,
                "word_count": len(text.split()) if text else 0
            })

    return extracted_data


if __name__ == "__main__":
    pdf_path = r"C:\Users\msvin\OneDrive\Desktop\sample.pdf"

    output = extract_text_from_pdf(pdf_path)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print("Structured extraction complete.")
