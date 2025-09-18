'''
# Qustion 1
larger_num = int(input("Enter the larger number:"))
smaller_num = int(input("Enter the smaller number:"))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1
    
print(f"number of times halved:{num}")

# Question 2

word = input("Enter a word: ")
result = ""
for i in range(1, len(word) - 1,2) :
    result += word[i]

print(f"Output = {result}")


# Question 3
# print even number btw 37 - 1050

number = 0
for number in range(37, 1051):
    if number % 2 == 0:
        print(number)
print("Even numbers between 37 and 1050 are:")

# Question 4
# single letter to newly created word
word = ""

while True:
    user_in = input("Enter a letter: ")
    if user_in == "done":
        break
    else:
        word += user_in
        
print(f"The final word is {word}")
'''

# Question 5
# calculate the sum of all odd numbers between 50 and 517

start = 50
end = 517