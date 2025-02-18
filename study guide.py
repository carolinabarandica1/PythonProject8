#for finding out results just use the print(type(...)) function
from urllib import response

print(type(2+3))
print(type(6/2))
print(type(2 != 3))
print(type(5 or 6))
print(type(print))
print(type(print(2*2)))
print(type("abc".find))
print(type("bubu"*2))
#print(type("bubu"*(4/2))) --> error
print(type(["abc", 2]))
print(type("abc"[2]))
print(type("abcabcabc".split("a")))


#for finding out results just use the print(...) function

print(2+3)
print(6/2)
print(2 != 3)
print(5 or 6)
print([1,2,3].append("John"))
print("bubu"*2)
#error  ---> print("bubu"*(4/2))
print(len(("abc", 2)))
print(2 + 3 * 2 ** 2)


#Assume that the operation are executed in order. What will each print display:
#just plug what he gives you
a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print((e[1::2]))
print(e+e[::-1])


#Write a function that takes the name of a text file as parameter. Print out the 3-
#letter words that start with “b”

import requests

def find_b_words(filename):
    # Step 1: Download the file from the link
    link = "https://gutenberg.org/cache/epub/77/pg77.txt"
    response = requests.get(link)  # Get the content from the URL

    with open(filename, 'wb') as file:
        file.write(response.content)  # Save the content to the file

    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            words = file.read().split()  # Read and split text into words
            for word in words:
                if len(word) == 3 and word.lower().startswith('b'):  # Check for 3-letter words starting with 'b'
                    print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")  # Error message if file is missing


filename = "The_House_of_the_Seven_Gables.txt"
find_b_words(filename)


#Write a function that takes an integer as parameter and returns a list of all the
#divisors of that number:


def find_divisors_of_n(n):
    try:
        return [i for i in range(1, n + 1) if n % i == 0]
    except TypeError:
        print("Error: Input must be an integer.")

print(find_divisors_of_n(28))


#Write a function that forces the user to enter a multiple of 6 number. Use try,
#except to catch invalid inputs. Return that number

def get_multiple_of_6():
    while True:
        try:
            num = int(input("Enter a multiple of 6: "))
            if num % 6 == 0:
                return num
            else:
                print("That's not a multiple of 6. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

result = get_multiple_of_6()
print(f"You entered a valid multiple of 6: {result}")


#tuple
#a sequence of value much like a list

a_1=()
print(a_1)
a_2=(1,3,5,2,54)
print(a_2)
a_3=("me", "myself", "eye")
print(a_3)
print(type(a_1))
print(type(a_2))
print(type(a_3))


#As opposed to lists, tuples are immutable! You can not
#change them once they have been defined
#You can construct a tuple via the built in function: tuple
# We use the bracket operator to access elements in the tuple, just like a string or list

print(len(a_2))

#dictionaries
#A dictionary is a more general type of list. While in a list the indices are integers, in
#a dictionary they can be almost any immutable object. In the case of dictionaries,
#the index is called a “key”. Like indices, the “keys” need to be unique and each key
#maps to a value. Dictionaries are mutable

#A dictionary is created with {}

dic = {"uno", "one","two", "dos","three", "tres"}
print(len(dic)) #6
print(dic)  #{'uno', 'three', 'one', 'two', 'tres', 'dos'}

dic_2 = {"uno": "one", "two": "dos", "three": "tres", "love":"amor", "health":"salud"}
del dic_2["love"]
print(dic_2)
