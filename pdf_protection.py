from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

input_pdf = "collegereport.pdf"
output_pdf = "locked_report.pdf"
password = "ksit123"

c = canvas.Canvas(input_pdf, pagesize=letter)
c.drawString(100, 750, "Confidential Report")
c.drawString(100, 730, "This is a demo PDF created for password protection example.")
c.save()

reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)
    
writer.encrypt(password)

with open(output_pdf, "wb")as f:
    writer.write(f)
    
print("✅ PDF protected successfully! Saved as", output_pdf)
