import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def load_data(csv_path):
    """Load data from a CSV file."""
    return pd.read_csv(csv_path)

def generate_report(data, report_title, output_path="report.pdf"):
    """Generate a PDF report from the data."""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, report_title)

    # Date
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table headers
    c.setFont("Helvetica-Bold", 10)
    y = height - 120
    x = 50
    for col in data.columns:
        c.drawString(x, y, str(col))
        x += 100

    # Table data
    c.setFont("Helvetica", 9)
    y -= 20
    for index, row in data.iterrows():
        x = 50
        for item in row:
            c.drawString(x, y, str(item))
            x += 100
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print(f"Report generated at: {output_path}")

if __name__ == "__main__":
    csv_path = "sample_data.csv"  # Replace with your CSV file
    data = load_data(csv_path)
    generate_report(data, "Automated System Report")
