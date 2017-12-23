def function_basic():
    print("This is a function.")


def function_basic_return(a, b):
    return a + b


def function_args(name, age):
    print(name, "is", age, "years old.")


def function_args_default(name, age=12):
    print(name, "is", age, "years old.")


def function_args_keyword(name, age=12, gender="boy"):
    print(name, "is", age, "years old", gender)


def function_args_flexible_numbers(*args):
    print(type(args))
    total = 0
    for i in args:
        total += i
    print(total)


function_args_keyword("Lucy", gender="girl")
function_args_flexible_numbers(1, 2, 3)

child = ["Tom", 12, "boy"]
# Unpacking args
function_args_keyword(*child)
