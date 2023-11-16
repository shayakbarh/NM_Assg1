"""
    Python code that prints each character of the string "mumbai" 
    and its Unicode code point and sum of these Unicode code points    
"""

S = 'mumbai'

unicode_sum = 0

for char in S:
    print(f"Character: {char}, Unicode Code Point: {ord(char)}")

    unicode_sum += ord(char)
    

print(f"\nSum of Unicode Code Points: {unicode_sum}")
