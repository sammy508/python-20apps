from pathlib import Path
import pandas as pnd
import glob
from fpdf import FPDF

filepaths = glob.glob("app3(pdf-voice)/invoices/*.xlsx")
print(len(filepaths))

for filepath in filepaths:
    df = pnd.read_excel(filepath,sheet_name="Sheet 1")
    pdf = FPDF(orientation="p",unit="mm",format="A4") 
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr,date = filename.split("-")
    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = f"Invoice nr. {invoice_nr}",ln=1)
    
    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = f"Invoice nr. {date}",ln=1)

    pdf.output(f"app3(pdf-voice)/pdf/{filename}.pdf")
    

