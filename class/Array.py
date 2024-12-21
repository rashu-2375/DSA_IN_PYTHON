# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#    3. March - 2600
#    4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

exp = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print("extra amount is",exp[1] - exp[0])   #150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:", exp[0] + exp[1] + exp[2]) #Expense for first quarter: 7150

# 3. Find out if you spent exactly 2000 dollars in any month  
print("Did I spent 2000$ in any month? ", 2000 in exp)  # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp) #[2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
exp[3] = exp[3] - 200
print(exp)  #[2200, 2350, 2600, 1930, 2190, 1980]



# You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
l = 0 
for i in heros:
    l += 1
print("length of list:", l)  #5

# Add 'black panther' at the end of this list
heros.insert(5,'black panther')
# heros.append('black panther')
# print(heros)

heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)


#  4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)


heros.sort() #sort hogi list in alphabetical order
print(heros)


max_no = int(input("Enter max_no"))
odd_numbers = []
for i in range(1, max_no):
    if i % 2 != 0:
        odd_numbers.append(i)
# Enter max_no 60
# Odd numbers: 
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
print("Odd numbers: ", odd_numbers)
