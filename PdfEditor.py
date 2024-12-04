from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os

def add_service_number_to_pdf(pdf_path, service_number, output_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    for page_number, page in enumerate(reader.pages):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        can.setFont("Helvetica-Bold", 20)
        can.setFillColorRGB(1, 1, 1)

        x_pos = width / 2 - 60
        y_pos = height - 110
        can.drawString(x_pos, y_pos, f"{service_number}")

        can.save()
        packet.seek(0)

        overlay = PdfReader(packet)
        page.merge_page(overlay.pages[0])

        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

@staticmethod
def process_all_pdfs_in_directory():
    files = [f for f in os.listdir() if f.endswith('.pdf')]

    for file_name in files:
        try:
            service_number = file_name.split(' ')[1]
        except IndexError:
            print(f"Could not extract service number from file: {file_name}")
            continue
        
        #same name to override the original file
        output_file_name = file_name
        
        print(f"processing: {file_name} -> {output_file_name}")
        add_service_number_to_pdf(file_name, service_number, output_file_name)

# if __name__ == "__main__": 
#     process_all_pdfs_in_directory()
# for using only this script without the main.py