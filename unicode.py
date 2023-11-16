"""
    Python code to print each character of the string "mumbai" 
    and its Unicode code point and sum of these Unicode code points
    and to create a list that contains the Unicode code points of the characters in S using list comprehension  
"""

S = 'mumbai'

unicode_sum = 0


for char in S:
    print(f"Character: {char}, Unicode Code Point: {ord(char)}")

    unicode_sum += ord(char)
    

print(f"\nSum of Unicode Code Points: {unicode_sum}")


# create a list using list comprehension

unicode_list_comprehension = [ord(char) for char in S]
print("\nUsing List Comprehension:", unicode_list_comprehension)


