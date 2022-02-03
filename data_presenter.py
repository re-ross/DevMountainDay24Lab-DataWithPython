cupcake_invoices = open('CupcakeInvoices.csv')

# for row in cupcake_invoices:
#     print (row)
     

# for row in cupcake_invoices:
#     values = row.split(',')
#     print(values[2])


# for row in cupcake_invoices:
#     values = row.split(',')
#     total = round((float(values[3]) * float(values[4])),2)
#     print(total)

total = 0

for row in cupcake_invoices:
    values = row.split(',')
    total = round(total) + (float(values[3]) * float(values[4]))

print (total)

cupcake_invoices.close()



