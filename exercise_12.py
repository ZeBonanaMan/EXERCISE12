income = 45000
tax_payable = 0

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    temp_tax = income - 10000
    tax_payable = temp_tax * .10
else:
    tax_payable += 10000 * 0
    tax_payable += 10000 * .10
    tax_payable += (income - 20000) * .20

print("Given income:", income)
print("Total tax to pay is:", tax_payable)