# langdoc-ocr

## 概要

PDFからテキストを抽出するOCRを行う。

## 準備

- poppler
- tesseract

をインストールする。

popplerを落としてきてpathを通す。  
Windowsの場合：
```powershell
$env:path +=';C:\path\to\poppler\bin\'
```

tesseractをインストール（WindowsならUB Mannheimのインストーラーが楽）
```powershell
$env:path +=';C:\path\to\tesseract\'
```

## 実行

```bash
python main.py
```