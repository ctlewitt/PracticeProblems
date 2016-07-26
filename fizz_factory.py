# This takes a dict of number: string key-value pairs and prints out the numbers up to 100,
# replacing numbers with the strings that are the values of any keys that are factors of the number
# like FizzBuzz

#END = 21
END = 101 # range excludes upper bound

def fizz_factory(fizz_dict):
    if fizz_dict is None:
        print(*range(1,END), sep="\n")
        return
    for num in range(1, END):
        printed = False
        for key, val in fizz_dict.items():
            if num % key == 0:
                print(val, end="")
                printed = True
        if not printed:
            print(num, end="")
        print()

dict1 = {2: "!", 3: "@", 5: "$", 7: "%", 11: "^", 13: "&"}
dict2 = {}
dict3 = None
dict4 = {2: "hi", 3: "world", 4: "!"}

fizz_factory(dict1)
fizz_factory(dict2)
fizz_factory(dict3)
fizz_factory(dict4)