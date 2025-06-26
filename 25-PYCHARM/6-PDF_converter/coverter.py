from pdf2docx import Converter

pdf_file_path = "samplePDF.pdf"

output_path = "output.docx"

docx = Converter(pdf_file=pdf_file_path)
docx.convert(output_path)
docx.close()