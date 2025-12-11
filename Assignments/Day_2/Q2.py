# Q2 : Count Even and Odd Numbers
# Take a list of numbers as input (comma-separated).
# Count how many are even and how many are odd.
# Print results.

len=int(input("Enter the size of list : "))
print("Enter List elements : ")

list = list(map(int,input("Enter numbers (comma-separated): ").split(',')))      #Comma saperated list as a string string

# for i in range(len):
#     i=int(input())
#     list.append(i)

evenCnt=0
oddCnt=0
for i in list:
    if i % 2 == 0:
        evenCnt+=1
    else :
        oddCnt+=1
        
print(f"Count of Even numbers in list : {evenCnt}")
print(f"Count of Odd numbers in list : {oddCnt}")