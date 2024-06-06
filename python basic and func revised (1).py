###Introduction to Python 
''

###Input and Output Statements Example 
name = input("Enter your name: ")
print("Hello, " + name + "Welcome.")

''

''

###Print function with keyboard arguments (sep, end)
print("Python", "is", "awesome", sep=" ", end="!\n")

''

''

###Data Types in python(str, int, float, complex)
my_string = "OpenAI"
my_integer = 42
my_float = 2.71828
my_complex = 4 + 5j
print("String:", my_string, "Type:", type(my_string))
print("Integer:", my_integer, "Type:", type(my_integer))
print("Float:", my_float, "Type:", type(my_float))
print("Complex:", my_complex, "Type:", type(my_complex))


''

''
###Expression, Operators, type casting

a = 5
y = "10"
n = int(y)  
result = a + n
print(result)  

''

''

###Conditional Statements - 

juice = input("Enter the type of juice (apple, orange, or grape): ")
if juice == "apple":
    print("You selected apple juice.")
elif juice == "orange":
    print("You selected orange juice.")
elif juice == "grape":
    print("You selected grape juice.")
else:
    print("Sorry, notavailable.")


''

''
###looping statements 

#for loop - used for iterating over a sequence.
name = ["abhi", "bob", "cherry"]
for name in name:
    print(name)

#while loop - allows code to be executed repeatedly based on a given Boolean condition.
count = 0
while count < 9:
    print("Count:", count)
    count += 1

#Nested loops - loops inside other loop.
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

''

''

###jumping statements 
#Break Statement - used to terminate the loop
for i in range(7):
    if i == 5:
        break
    print(i)
    
#continue statement - used to skip the current iteration and proceed to the next iteration of the loop.
for i in range(7):
    if i == 5:
        continue
    print(i)

#Pass Statement - used as a placeholder for future code.
for i in range(7):
    if i == 5:
        pass
    else:
        print(i)

''

''

###Some examples

#len() function - returns the length.
my_string = "Hello Audience!"
print(len(my_string)) 

#id() function - unique identifier.
x = 7
print(id(x))  

#type() function - returns the type of an object.
y = 3.147
print(type(y))  

#range() function - generates a sequence of numbers.
for i in range(7):
    print(i)  

''

###Python Functions 
#Lambda Function
add = lambda x, y: x + y
print(add(6,8))
#map function
numbers = [2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
#reduce function
numbers = [1,2,3,4]
product = reduce(lambda x, y : x * y, numbers)
print(product)
#filter function
numbers = [1,2,3,4,5,7 ]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

#global keyword , return keyword left 


###10.1
import math
def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        (radius,) = dimensions
        return math.pi * (radius ** 2)
    else:
        return "Unknown Shape"
    
    
###10.2
def reverse_words(text):
  return " ".join(text.split()[::-1])

###10.3
def analyze_list(numbers):
    if not numbers:
        return {"min": None, "max": None, "average": None}
    
    min_value = min(numbers)
    max_value = max(numbers)
    average_value = sum(numbers) / len(numbers)
    
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }

###10.4
#Start your code from here.
def filter_short_names(names, max_length):
    return list(filter(lambda name: len(name) < max_length, names))

###10.5
def analyze_text(text):
    words = text.split()
    
    word_count = len(words)
    
    char_count = sum(len(word) for word in words)
    
    words_lower = [word.lower() for word in words]
    
    word_freq = {}
    
    for word in words_lower:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    most_frequent_word = max(word_freq, key=word_freq.get)
    
    analysis = {
        'word_count': word_count,
        'char_count': char_count,
        'most_frequent_word': most_frequent_word
    }
    
    return analysis


