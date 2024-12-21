def function_1(x,y):
    try:
        return function_2(x,y)
    except:
        return float('inf')
def function_2(x,y):
    try:

        return function_3(x,y)
    except:
            return 0.0
def function_3(x,y):
    return x/y # crash here

print(function_1(1,0))
    