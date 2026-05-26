import string
# string is used so we can access the ascii_letters, digits, and punctuation constants to create a strong password.
import random
#random is used to generate random characters for the password.
length=int(input("Enter the desired length of the password: "))
characters=string.ascii_letters + string.digits + string.punctuation
# string.ascii_letters includes both uppercase and lowercase letters, string.digits includes numbers, and string.punctuation includes special characters.
password=''.join(random.choice(characters) for i in range(length))
# join is used to concatenate the randomly chosen characters into a single 
# random.choice() is used to select a random character
# ''is used to specify that there should be no separator between the characters in the final password.if we use _ there will be a_b_c if ' ' then a b c  and if ''then anc
print("Generated password:", password)