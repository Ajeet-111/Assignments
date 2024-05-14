# Q. 1 - What is github? Write a simple definition for github.
print("\nQ.1 answer:")
print("Github is a platform where you can save your code, update your skills,\nshare your experience and you can associate with others too this \napp helps you in saving your coding journey for no cost.") 


# Q. 2 - How can you clone a GitHub repository to your local machine? Provide the command and explain each part of it.
print("\nQ.2 answer:")
print("it's a long process which involves copying an url from your repository and pasting it\non gitbash after the command 'git clone' then you require to login on github to verify\nthat it's you, after this process you open the clone folder in git bash, followed by \nthree important commands, it completees your process of making a clone.")


# Q. 3 - Given the list fruits = ['apple', 'banana', 'cherry', 'date'], how would you access the “na” from the ‘banana’? after that change it in upper case like “NA”
print("\nQ.3 answer:")

fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[1][4:])
print(fruits[1][4:].upper())


# Q. 4 - What is tuple unpacking? Provide an example with the tuple coordinates = (10, 20, 30), to complete this assignment question, you can take reference from the internet, and describe the tuple unpacking by a coding example. 
print("\nQ.4 answer:")

coordinates = (10, 20, 30)
(a,b,c) = coordinates

print(a)
print(b)
print(c)