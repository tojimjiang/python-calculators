#Introduction  Text
print('Hello! I\'m here to help you calculate your tip')
#bill ammount
bill = float(input('How much was your bill? (enter as a number without dollar signs or commas): '))
#tip percent
tip = float(input('How much tip would you like to leave? (enter just a number percentage): ')) / 100
print('Thanks!')
#print information
print('You need to leave $', float(format(bill * tip,'.2f')),' as a tip.', sep='')
print('Your total bill will be $', tip_amt + bill, sep='')
