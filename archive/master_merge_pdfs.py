import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
import io

def create_nametag(data, template_path, output_path):
    # Create a canvas object using ReportLab
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    print("data:", data)

    # Register font
    pdfmetrics.registerFont(TTFont('FuturaPTBold', './FuturaPTBold.ttf'))

    # Set font to white
    can.setFillColor(white)
    
    # Write name
    can.setFont("FuturaPTBold", 140)  # Change the font size as needed
    x_name, y_name = 100, 650  # Adjust as necessary
    can.drawString(x_name, y_name, data['name'])

    # Write company
    can.setFont("FuturaPTBold", 90)  # Change the font size as needed
    x_organization, y_organization = 100, 500  # Adjust as necessary
    can.drawString(x_organization, y_organization, data['organization'])

    # Write title
    can.setFont("FuturaPTBold", 60)  # Change the font size as needed
    x_occupation, y_occupation = 100, 200  # Adjust as necessary
    can.drawString(x_occupation, y_occupation, data['occupation'])

    # Save the canvas content to the packet
    can.save()
    
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    
    # Create a new PDF with ReportLab content
    new_pdf = PdfReader(packet)

    # Save the new PDF for debugging
    with open("./test.pdf", "wb") as f:
        output_debug = PdfWriter()
        output_debug.add_page(new_pdf.pages[0])
        # output_debug.add_page(new_pdf)
        output_debug.write(f)
    
    # Read the existing template PDF
    existing_pdf = PdfReader(open(template_path, "rb"))
    
    # Create a PdfFileWriter object to merge PDFs
    output = PdfWriter()
    
    # Get the first page of the template PDF
    template_page = existing_pdf.pages[0]

    # Merge the new PDF (with the added text) onto the template PDF
    template_page.merge_page(new_pdf.pages[0])

    # Add the merged page to the PdfFileWriter object
    output.add_page(template_page)
    
    # Write the output PDF to a file
    with open(output_path, "wb") as outputStream:
        output.write(outputStream)

def main(csv_file, template_pdf, output_dir):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    for index, row in df.iterrows():
        # Define the output PDF path for each nametag
        output_path = f"{output_dir}/nametag_{index+1}.pdf"
        
        # Create a dictionary with the data for the current row
        data = {
            'name': row['name'],
            'occupation': row['occupation'],
            'organization': row['organization']
        }
        
        # Generate the nametag
        create_nametag(data, template_pdf, output_path)


csv_file = "sample_data1.csv"
template_pdf = "./template.pdf"
output_dir = "./output"

main(csv_file, template_pdf, output_dir)
