""" members = {
    'account1'  : 13 ,
    'account2'  : 12 ,
    'account3'  : 15 ,
}

# members = {}
members.clear()

print(members) """

members = {
    'account1'  : 13 ,
    'account2'  : 12 ,
    'account3'  : 15 ,
}

another =  {
    'account4'  : 13 ,
    'account5'  : 12 ,
}

members.update(another)

print(members)