testProc([1, 2, 3]) # Explicitly passing in a list
testProc() # Using a default empty list
def testProc(n = []):
# Do something with n
print n     '''Error: syntax error in python3 n should be enclosed in brackets and 
               NameError, n is local to function testProc and it cannot be accessed outside of it.'''
