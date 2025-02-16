from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm
import pickle
import os

def ocr_scanned_pdf(pdf_path: str, name: str, lang: str):
    # convert pdf to image
    images = convert_from_path(pdf_path)

    # ocr
    texts = f"# {name}\n"
    lst_texts = []

    for i, image in tqdm(enumerate(images)):
        text = pytesseract.image_to_string(image, lang=lang)
        texts += f"## page {i}\n{text}\n\n"
        lst_texts.append(text)

    # save pkl
    if not os.path.exists("data/pkl"):
        os.makedirs("data/pkl")
    pickle.dump(lst_texts, open(f"data/pkl/{name}.pkl", "wb"))
    
    # save texts
    if not os.path.exists("data/texts"):
        os.makedirs("data/texts")
    with open(f"data/texts/{name}.txt", "w", encoding="utf-8") as f:
        f.write(texts)

def main():
    ocr_scanned_pdf("data/pdf/test.pdf", "data/img/test")

if __name__ == "__main__":
    main()
