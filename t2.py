class A(object):
    def print_it(self):
        print('A')
        self.val=3

class B(A):
    def print_it(self):
        print('B')

b=B()
b.print_it()            #Prints B  - the recent class.
try:
   print ("b is %d"%b.val)
except AttributeError:
   print("b has not yet been initialized")

super(B, b).print_it()  #object b base class 
print ("B is %d"%b.val)
