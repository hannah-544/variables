'''print is an output variable by itself'''
'''local variables are accessed inside the funtion 
global variables ara accessed outside the function'''
age = 10  #global variable(everywhere)
def mwangi():
     age = 16 #local variable(inside function:preference will always be given in this variable)
     print("now " ,age)

mwangi()
print('before', age)

'''specify a global variable'''

v = 5 #global variable(everywhere)
print(id(v))
def mwangi():
    v=10

    x=globals()['v'] #specifies the global variables
    print(id(x))
    print("in fun " ,v)

    globals()['v']=15 #change global variable without affecting local var



mwangi()
print('outside', v)

