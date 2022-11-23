import openpyxl
pylocation=openpyxl.load_workbook("C:\\Users\\lm\\excel\\sheet1.xlsx")#loading path
sheet=pylocation.active
dict={}
cell=sheet.cell(row=1,column=2)
print(cell.value)
sheet.cell(row=1,column=2).value="Niloy"
print((sheet.cell(row=1,column=2).value))
print(sheet.max_row)
print(sheet.max_column)
print(sheet['A3'].value)
for i in range(1,sheet.max_row+1):#i=1 j=1234 then i=2 j=......... #i for roe
    if sheet.cell(row=i,column=1).value == "testcase2":
        for j in range(1,sheet.max_column+1):#j for column

            #print(sheet.cell(row=i,column=j).value)#will print the value of all existing index
            #dict["name"]="Nahid"
            #dict["name"]=sheet.cell(row=i,column=j).value
            dict[sheet.cell(row=1,column=j).value] = sheet.cell(row=i,column=j).value
print(dict)







