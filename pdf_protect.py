from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# File names
sample_pdf = "sample.pdf"
protected_pdf = "protected.pdf"

# Step 1: Create a sample PDF
c = canvas.Canvas(sample_pdf, pagesize=letter)
c.drawString(100, 750, "Confidential Report")
c.drawString(100, 730, "This is a demo PDF created for password protection example.")
c.save()

# Step 2: Protect the PDF
reader = PdfReader(sample_pdf)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Add password
writer.encrypt("mypassword123")

with open(protected_pdf, "wb") as f:
    writer.write(f)

print("✅ PDF protected successfully! Open 'protected.pdf' with password: mypassword123")
