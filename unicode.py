"""
    Python code to print each character of the string "mumbai" 
    and its Unicode code point and sum of these Unicode code points
    and to create a list that contains the Unicode code points of the characters in S using list methods   
"""

S = 'mumbai'

unicode_sum = 0

unicode_list_method = []

for char in S:
    print(f"Character: {char}, Unicode Code Point: {ord(char)}")

    # create a list using list method
    unicode_list_method.append(ord(char))

    unicode_sum += ord(char)
    

print(f"\nSum of Unicode Code Points: {unicode_sum}")

print("\nUsing List Methods:", unicode_list_method)
