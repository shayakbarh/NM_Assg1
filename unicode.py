"""
    Python code to print each character of the string "mumbai" 
    and its Unicode code point and sum of these Unicode code points
    and to create a list that contains the Unicode code points of the characters in S using map class  
"""

S = 'mumbai'

unicode_sum = 0


for char in S:
    print(f"Character: {char}, Unicode Code Point: {ord(char)}")

    unicode_sum += ord(char)
    

print(f"\nSum of Unicode Code Points: {unicode_sum}")


# creating a list using map class

unicode_map = list(map(ord, S))
print("\nUsing Map Class:", unicode_map)




