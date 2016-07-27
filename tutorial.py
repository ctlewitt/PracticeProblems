# this is from a workshop I attended about generators, list comprehensions, map, fold, etc

from collections import Counter
import random

def hello_everyone(names):
    greetings = []
    for name in names:
        greeting = "hello, " +name
        greetings.append(greeting)
    return greetings


def make_greeting(name):
    return "hello, " + name


def make_greetings(names):
    return map(make_greeting, names)

res = []
for x in nums:
    res.append(make_greeting(str(x+1))

)

#comprehension
nums = range(10)
res = [make_greeting(str(x+1)) for x in nums]

def is_odd(x):
    return x % 2 != 0

filter(is_odd, range(10))

[x for x in range(10) if is_odd(x)]

[is_odd(x) for x in [1,2,3,4,5] if x>3]

s= set()
s.add(3)
s.add(4)
3 in s
6 in s

nums = [2,2,2,3,4,4,4,5,3,3,3,1,4,4,9,6,9]
list(set(nums)) # puts each thing in the list into the set and then it's unique

strs = ["asd", "abc", "asdf", "erty"]
{len(s) for s in strs}

#these were set comprehensions; we just did list comprehensions

{s: len(s) for s in strs}
#that was a dictionary comprehension; super powerful stuff

{x: is_odd(x) for x in range(10)}

c = Counter([True, False, True])
c.update([True])

c = Counter([is_odd(x) for x in [1,2,3,4,5,6,7,6]])
c[True]
c[False]

#lots of good stuff in Collections library

for l in {"a":1, "b":2, "c":3}:
    print l #prints the keys

for line in open("my_file.txt"):
    print line #prints each line

[len(line) for line in open("my_file.txt")]

# you can define things that can be iterated over and how they can be iterated over
# class that takes a list and iterates over the list in random order
class RandomOrder(object):

    def __init__(self, li):
        self.li = li
        self.order = range(len(li))
        random.shuffle(self.order)

    def __iter__(self): # an interable is something with this method; this returns an iterator (has next function)
        self.index = 0
        return self #common pattern to return somethign that is both an iterator and iterable

    def next(self):
        if self.index >= len(self.order):# or random.random() < 0.2:
            #random.shuffle(self.order) # this would give us a new order the next time we iterate through the list
            raise StopIteration()
        ret = self.li[self.order[self.index]]
        self.index +=1
        return ret

#for x in iterable:
#    do_stuff(x)

#iterator = xs.__iter__()
#while True:
#    try:
#        x = iterator.next()
#        do_stuff(x)
#    except StopIteration:
#        break


class RandomOrderIterator(object):

    def __init__(self, li):
        self.li = li
        self.order = range(len(li))
        random.shuffle(self.order)
        self.index = 0

    def next(self):
        if self.index == len(self.order):
            raise StopIteration()
        ret = self.li[self.order[self.index]]
        self.index += 1
        return ret

class RandomOrderIterable(object):
    def __init__(self, li):
        self.li = li

    def __iter__(self):
        return RandomOrderIterator(self.li)

def random_order(li): #functions with "yield" in them, become generators; they are iterators
    order = range(len(li))
    random.shuffle(order)
    for index in order:
        yield li[index]


strs = ["abc", "asd", "sadf", "erty"]

# not reusable:
for s in strs:
    if len(s) == 4:
        break

lengths = [len(s) for s in strs]
for l in lengths: #not great
    if l == 3:
        print "hello"

def lengths(strs): #use this generator instead of the code above
    for s in strs:
        yield len(s)

for l in lengths(strs): #uses the generator above
    if l == 3:
        print "hello"
        break


#generators are easierways to write iterators

#decorators: higher order functions (functions return functions)
def adder(x):
    def inner(y):
        return x + y
    return inner

f = adder(2)
f(6) # gives back 8

adder(5) (10) #gives back 15

def logger(f)
    def wrapper():
        print "about to call"
        f()
        print "done calling!"
    return wrapper

@logger
def my_function():
    print "in my function!"


my_function = logger(my_function)

def retry(f):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return f(*args, **kwargs)
            except Exception:
                pass
    return wrapper

@another_decorator
@retry
def call_internet():
    if random.random() < 0.1:
        raise Exception("call failed!")
    else:
        return "success!"


#this says when you call call_internet() that it actually calls retry(call_internet)
#call internet = another_decorator(retry(call_internet))

#can use this to call a memorizer???  can you write one yourself?

#********************write a cache/memoizing decorator to make sure you understand this



# decorators
# functions that take functions and return functions
# you call the function just the same and then the decorator is executed

def logged(func):
    print("I am about to execute")
    func()
    print("I just executed the function")

def hello():
    return "hello world"

hello = logged(hello)

@logged
def hello():
    return "hello world"

#*args can receive any number of arguments

def logged(f):
    name = f.__name__
    def wrapper(*args):
        print ("about to call {}".format(name))
        ret_val = f(*args)
        print("just called {}".format(name))
        return ret_val
    return wrapper