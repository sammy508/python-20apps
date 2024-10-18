from pathlib import Path
import pandas as Pd
import glob as glob
import fpdf as FPDF

filepaths = glob.glob("app3(pdf-voice)\exercise\invoices/*")
print(len(filepaths))
for files in filepaths:
    # df = Pd.read_csv(files)
    pdf = FPDF(orientation="p",unit="mm",format="A4") 

    pdf.add_page()
    filename = Path(filename).stem
    name = filename.title()
    
    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt=name, ln=1)
pdf.output("Output.pdf")

