ex 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

ex 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

ex 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

ex 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#example 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)  #convert tuple into a list to change it

#example 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)     #unpacking