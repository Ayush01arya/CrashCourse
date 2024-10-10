# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise

s=input()
into=s.lower()
new_string=""
for char in into:
    if char.isalnum() or char == " ":
        new_string += char

if(new_string==new_string[::-1]):
    print(True)
else:
    print(False)

# if s=="":
#     print(True)
# else:
#     print(False)
