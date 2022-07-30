"""
* CS50P Problem Set 8
* Shitificate
* by Samu Reinikainen 30.07.2022
"""

from fpdf import FPDF

def make_shirt(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 0, "CS50 Shirtificate", new_x="LEFT", new_y="NEXT", align="C")
    pdf.set_y(60)
    pdf.image("shirtificate.png", w=pdf.epw, h=0)
    pdf.set_y(140)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 0, name, new_y="NEXT", align="C")
    pdf.ln(20)
    #pdf.set_y(160)
    pdf.cell(0, 0, "took CS50", new_y="NEXT", align="C")
    pdf.ln(10)
    #pdf.set_y(200)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 0, "(and survived)", new_y="NEXT", align="C")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter name: ").strip()

    if len(name) > 0:
        make_shirt(name)
    else:
        exit()

if __name__ == "__main__":
    main()
