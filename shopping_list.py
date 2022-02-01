tomatoes = 0.87 #pack of 6
sugar = 1.09 #500g
sponge = 0.29 #pack of 10
juice = 1.89 #per 1.5l bottle
foil = 1.29 #per 30m roll

sugar_kg = sugar * 2
print("1kg of sugar is: £", sugar_kg)

total_bill = (sponge * 2) + (juice * 2) + (tomatoes * 2)
print("Total bill is: £", total_bill)


new_bill = tomatoes + ((sponge/10) * 3) + ((juice/1.5) * 1) + ((foil/30)*20) + (sugar_kg * 0.18)
print ("£", new_bill, " per person")

total = 5 * new_bill
print("For five people, the bill comes to: £",total)

bill_five_VAT = total * 1.2 #multiply price by 1.2 to add VAT
print("Bill with VAT: £", bill_five_VAT)

#show float to 2 decimal places
format_float = "{:.2f}".format(bill_five_VAT)
print("£", format_float)