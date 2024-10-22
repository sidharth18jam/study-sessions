import openpyxl
import re
from datetime import datetime
from dateutil import parser
# Load the workbook and select the sheet
wb = openpyxl.load_workbook('yourfile.xlsx')
sheet = wb.active  # Or wb['SheetName'] if you know the sheet
desiredDateFormat = "%d-%m-%Y %H:%M"
# Loop through all rows and columns
for row in sheet.iter_rows():
    for cell in row:
        if isinstance(cell.value, str):  # Check if the cell contains a string
            # String manipulations: Strip whitespaces, uppercase the text, etc.
            try:
                parsedDate = parser.parse(cell.value)
                cell.value = parsedDate.strftime(desiredDateFormat)
            except (ValueError, TypeError):
                cleaned_value = cell.value.strip()
            
            # Use regex to remove unwanted characters or extra spaces
                cleaned_value = re.sub(r'\s+', ' ', cleaned_value)  # Replace multiple spaces with one space
                cleaned_value = re.sub(r'[^\w\s@.-]', '', cleaned_value)  # Remove non-alphanumeric characters
            
            # Update the cell with cleaned value
                cell.value = cleaned_value.upper()
        
        elif isinstance (cell.value, datetime):
            cell.value = cell.value.strftime(desiredDateFormat)

            


# Save the cleaned Excel file
wb.save('cleaned_data.xlsx')
