# Q1:Write a Python program that takes a sentence from the user and prints:
# Number of characters
# Number of words
# Number of vowels

str=input("Enter the string : ")
chrlen=0

# No of chars
for i in str :
    if i != " ":
        chrlen+=1
print(f"Number of characters (without Space) in {str} : {chrlen}")

# No of words
splt=str.split()
print(f"Number of words in {str} : {len(splt)}")

# No of vowels
vowels="aeiouAEIOU"
vowellen=0
for i in str :
    if i in vowels:
        vowellen+=1
print(f"Number of vowels in {str} : {vowellen}")

