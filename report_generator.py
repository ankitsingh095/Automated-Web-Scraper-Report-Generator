import pandas as pd

# Load scraped donor data
df = pd.read_json("scraper/output/donors.json")

# Group donors by blood group
grouped = df.groupby("blood_group").size().reset_index(name="count")

# Save Excel report
with pd.ExcelWriter("reports/donor_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Donors", index=False)
    grouped.to_excel(writer, sheet_name="Summary", index=False)

print("Report generated: reports/donor_report.xlsx")
