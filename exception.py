x=input("enter 1:")
y=input("enter 2:")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("exception is",e)
    z=None
except TypeError as e:
    print("exception type:",type(e).__name__)
    print('TypeError')
    z=None
except ValueError as e:
    print("exception type:",type(e).__name__)
    print('ValueError')
    z=None

print('Division is:',z)
