from pathlib import Path
import pandas as pnd
import glob
from fpdf import FPDF

filepaths = glob.glob("app3(pdf-voice)/invoices/*.xlsx")
print(len(filepaths))




for filepath in filepaths:
    pdf = FPDF(orientation="p",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr,date = filename.split("-")
    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = f"Invoice nr. {invoice_nr}",ln=1)
    
    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = f"Invoice nr. {date}",ln=1)
     
    df= pnd.read_excel(filepath,sheet_name="Sheet 1")

    # columns = list(df.columns)  instead we can do this to replace _ with space
    columns = [item.replace("_", " ").title() for item in df.columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8, txt=columns[0],border=1)
    pdf.cell(w=70,h=8, txt=columns[1],border=1)
    pdf.cell(w=30,h=8, txt=columns[2],border=1)
    pdf.cell(w=30,h=8, txt=columns[3],border=1)
    pdf.cell(w=30,h=8, txt=columns[4],border=1, ln=1)
    

    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=70,h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=30,h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30,h=8, txt=str(row["total_price"]),border=1, ln=1)

    total = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8, txt="",border=1)
    pdf.cell(w=70,h=8, txt="",border=1)
    pdf.cell(w=30,h=8, txt="",border=1)
    pdf.cell(w=30,h=8, txt="",border=1)
    pdf.cell(w=30,h=8, txt=str(total),border=1, ln=1)





    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = f"Total price is {total}",ln=1)

    pdf.set_font(family = "Times",size=16, style = "B")
    pdf.cell(w=50, h=8, txt = "Pyhton How")
    pdf.image("app3(pdf-voice)/004 pythonhow.png", w=10)

    pdf.output(f"app3(pdf-voice)/pdf/{filename}.pdf")
    

