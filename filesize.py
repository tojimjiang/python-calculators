#user input
file = float(input('Enter a file size, in kilobytes (KB): '))
#linegap
print()
# linegap
print(format(file,'.2f'), 'KB', '...')
#line gap
print()
#compacting:
dots = '... in'
#printing user info
print(dots, format('bits','<9'), format(format(file*1024*8,',.2f'),'>24s'), 'bits')
print(dots, format('bytes','<9s'), format(format(file*1024,',.2f'),'>24s'), 'bytes')
print(dots, format('megabytes','<9s'), format(format(file/1024,',.2f'),'>24s'), 'MB')
print(dots, format('gigabytes','<9s'), format(format(file/1024/1024,',.2f'),'>24s'), 'GB')