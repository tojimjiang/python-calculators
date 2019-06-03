#introduction statement
print('This program will project how much you can earn by investing money in a high-yield savings account over a 3 month period.')
#line gap
print()
#investment and rate
money = float(input('To begin, enter how much money you would like to initially invest (i.e. 500): '))
rate = float(input('Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: ')) / 12
#line gap
print()
print('------- Calculating --------')
#calculations for each value
money_one = format(money + float(format(money * rate, '.2f')), '.2f')
#month 2
money_two = format(float(money_one) + float(format(float(money_one) * rate, '.2f')), '.2f')
#month 3
money_three = format(float(money_two) + float(format(float(money_two) * rate, '.2f')), '.2f')
#linegap
money_s = format(money, '.2f')
#print results
print()
print('Month', 'Starting Balance    ','Interest  ','Ending Balance')
print('1    ', format(format(money, '.2f'),'<20s'), format(format(money * rate, '.2f'), '<10s'), money_one)
print('2    ', format(money_one,'<20s'),format(format(float(money_one) * rate, '.2f'), '<10s'), money_two)
print('3    ', format(money_two,'<20s'),format(format(float(money_two) * rate, '.2f'), '<10s'), money_three)
