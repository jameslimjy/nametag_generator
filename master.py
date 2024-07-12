import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
import io

def fit_text(can, text, font_name, initial_font_size, max_width):
    """Adjust font size to fit text within max_width."""
    font_size = initial_font_size
    while can.stringWidth(text, font_name, font_size) > max_width and font_size > 5:
        font_size -= 1
    return font_size

def create_nametag(data, template_path, output_path):
    print("\n")
    print(data)
    # Read the existing template PDF
    existing_pdf = PdfReader(open(template_path, "rb"))
    template_page = existing_pdf.pages[0]

    # Create a canvas object and draw directly onto the template PDF
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(1424.63, 2010.24))  # Adjust the canvas size to match template

    # Register fonts
    pdfmetrics.registerFont(TTFont('FuturaPTBold', './fonts/FuturaPTBold.ttf'))
    pdfmetrics.registerFont(TTFont('FuturaPTHeavy', './fonts/FuturaPTHeavy.ttf'))
    pdfmetrics.registerFont(TTFont('FuturaPTBook', './fonts/FuturaPTBook.ttf'))

    # Set font to white
    can.setFillColor(white)

    # Calculate max width available for name and organization (100 points margin on each side)
    max_width_name_org = 1424.63 - 100 * 2
    
    # Write name
    initial_font_size = 180  # Initial font size
    x_name, y_name = 100, 740  # Adjust as necessary for the template size
    font_size_name = fit_text(can, data['name'], "FuturaPTBold", initial_font_size, max_width_name_org)
    can.setFont("FuturaPTBold", font_size_name)
    print("font_size_name:", font_size_name)
    can.drawString(x_name, y_name, data['name'])

    # Write organization
    max_font_size_organization = font_size_name * 2 / 3  # Ensure company font size is at most 2/3 of the name font size
    initial_font_size = min(120, max_font_size_organization)  # Initial font size
    x_organization, y_organization = 100, 550  # Adjust as necessary for the template size
    font_size_org = fit_text(can, data['organization'], "FuturaPTHeavy", initial_font_size, max_width_name_org)
    font_size_org = min(font_size_org, max_font_size_organization)  # Ensure font size does not exceed the maximum allowed
    can.setFont("FuturaPTHeavy", font_size_org)
    print("font_size_org:", font_size_org)
    can.drawString(x_organization, y_organization, data['organization'])

    # Calculate max width available for occupation (400 points)
    max_width_occupation = 1424.63 - 200 * 2
    
    # Write title
    initial_font_size = min(85, font_size_org)   # Initial font size
    x_occupation, y_occupation = 100, 270  # Adjust as necessary for the template size
    font_size = fit_text(can, data['occupation'], "FuturaPTBook", initial_font_size, max_width_occupation)
    can.setFont("FuturaPTBook", font_size)
    print("font_size:", font_size)
    can.drawString(x_occupation, y_occupation, data['occupation'])

    # Save the canvas content to the packet
    can.save()
    
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    
    # Create a new PDF with ReportLab content
    new_pdf = PdfReader(packet)
    new_pdf_page = new_pdf.pages[0]

    # Create a PdfFileWriter object to write the final output
    output = PdfWriter()

    # Merge the canvas onto the template
    template_page.merge_page(new_pdf_page)
    
    # Add the merged page to the PdfWriter object
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
            'name': row['name'].title(),
            'occupation': row['occupation'].upper(),
            'organization': row['organization'].upper()
        }
        
        # Generate the nametag
        create_nametag(data, template_pdf, output_path)

csv_file = "nametag_input_data.csv"
template_pdf = "./template_nametag.pdf"
output_dir = "./output"

main(csv_file, template_pdf, output_dir)
