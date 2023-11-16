
# dividing 1 by 0,1,2,3,4,5

for i in range(6):
    # here i is the divisor
    try:
        result = 1/i
        print(f"1/{i} = {result}")
    except ZeroDivisionError:
        print(f"1/{i} = indeterminate")


 
        
