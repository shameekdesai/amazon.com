# import openpyxl module 
import openpyxl 

wb = openpyxl.load_workbook("c123.xlsx") 

# Get workbook active sheet 
# from the active attribute 
sheet = wb.active 
r = sheet.max_row
c = sheet.max_column
 # to read the link from the column 
for i in range(2,r):
    d = sheet.cell(row = i, column = 4)
    if d.value is None:
        print("no links found at row %d" % i)
    #else:
       # print(d.value)
    
#to write the value in the  coloumn 
for j in range(2,r):
    f = sheet.cell(row = j, column = c-1)
    #if f.value is None:
    f.value = "5000"
 
# the save() workbook method. 
wb.save("c123.xlsx") 