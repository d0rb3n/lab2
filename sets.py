ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#example 1
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#example 2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)