# numbers
print(8 + 2)
print(8 - 2)
print(8 * 2)
print(7 / 2)
print(8 ** 2)
print(7 // 2)

print("==========")

# str
s = "This is amazing"
print(s[2])
print(s[-2])
print(s[2: 4])
print(s[2: -4])
print(s[-4: -1])
print(s[-4: len(s)])
s1 = "Today "
s2 = "is a good day"
print(s1 + s2)
s = "Hello "
print(s * 3)

print("==========")

# list
a = [1, 2, 3, 4, 5, 6, 7]
b = [7, 8, 9]
print(a[2])
print(a[-2])
print(a[2: 4])
print(a[2: -2])
print(a[-4: -1])
print(a[-4: len(a)])
print(a + b)
a[2: 4] = [-3, -4, 13, 14]
print(a)

print("==========")

# set
fruits = {"apple", "banana", "orange", "peach", "pear", "peach"}
print(fruits)
for fruit in fruits:
    print(fruit)
fruits.remove("apple")
if "apple" in fruits:
    print("Today we can eat apple.")
else:
    print("Where is my favorite apple.")
fruits.add("apple")
if "apple" in fruits:
    print("Today we can eat apple.")
else:
    print("Where is my favorite apple.")

print("==========")

# dict
child = {}
print(type(child))
child = {"Tom": 12, "Lucy": 13}
print(child)
print(child["Tom"])
print(child.get("Tom"))
child["Sheldon"] = 14
child.update({"Ema": 13})
print(child)
del child["Sheldon"]
child.pop("Ema")
print(child)
print(type(child.items()))
for k, v in child.items():
    print(k, "is", v)
