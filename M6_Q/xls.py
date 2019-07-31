from openpyxl import Workbook


wb = Workbook()
sheet = wb.active
data = [
    ('Id','WName','Year','status','company'),
    (1001,"python",2019,1,"Heraizen"), 
    (1002,"web",2018,1,"Spaneos")
]

for row in data:
    sheet.append(row)

wb.save("student.xlsx")