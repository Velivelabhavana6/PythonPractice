import fitz  # PyMuPDF
import json

def pdf_to_json(pdf_path, json_path):
    doc = fitz.open(pdf_path)   #opening pdf
    pdf_data = {}   #Empty dic

    for page_num in range(len(doc)):         #Loop through pages and extract
        page = doc.load_page(page_num)        #Load page one by one
        text = page.get_text()                #Extract text only from that page
        pdf_data[f"page_{page_num + 1}"] = text  #Saving in to dict like keys

    with open(json_path, 'w', encoding='utf-8') as f:         #Saving data into Json
        json.dump(pdf_data, f, ensure_ascii=False, indent=4)  #utf suppports all chars and ascii prsvents non english char
  #json dump uses writes the dict in to file as a cleanly formatted JSon
    print(f"PDF content saved to {json_path}")

# Example usage
pdf_to_json("file.pdf", "output.json")
