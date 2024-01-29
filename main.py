import os.path

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",format="A4",unit="mm")
    pdf.add_page()
    filename=Path(filepath).stem
    invoice_nbr,date= filename.split("-")
    pdf.set_font(family="Times",size=16)
    pdf.cell(w=5,h=8,txt=f"Facture Num.{invoice_nbr}  ",ln=1)
    
    pdf.set_font(family="Times",size=16)
    pdf.cell(w=5,h=8,txt=f"Date:{date}  ")

    pdf.output(f"PDFS/{filename}.pdf")
