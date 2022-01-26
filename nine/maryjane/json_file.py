import  json


x={'name':'John', 'state of origin':'imo', 'quantity':6}


#y=json.dump(x)

print(json.dump(json.loads(x), indent=4, sort_keys=True))







# x=1
# y=x*x
#
# y=json.dump()
# print(y)