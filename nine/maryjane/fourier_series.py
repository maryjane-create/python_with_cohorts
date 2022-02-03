import  os

print(os.path.join('usr', 'spam', 'bin'))


myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C://Users//thankyou', filename))


print(os.path.abspath('.//Scripts'))




print(os.path.abspath('.'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C://Ubuntu', 'C://'))

print(os.getcwd())
os.path.getsize('C://Ubuntu//System32//calc.exe')

path='C://linux//System32//calc.exe'


































# print(os.path.isabs(os.path.abspath('.')))
# print(os.path.abspath('.//Scripts'))

























































# data = {'name': 'arinze',
#        ' city': 'lagos'
#        }
#
# print(data['name'])