# sleepsort: write a function that takes a list of numbers and prints each number n after an n-second delay

import asyncio

# playing with doing it asynchronously; there is no need to sort here
def sleep_sort(my_arr):
    tasks = [my_waiter(num) for num in my_arr]
    loop.run_until_complete(asyncio.wait(tasks))

@asyncio.coroutine
def my_waiter(num):
    yield from asyncio.sleep(num)
    print(num)


#

# asynchronous execution
loop = asyncio.get_event_loop()
sleep_sort([3,1,4])
sleep_sort([3, 3, 3,1,4])
loop.close()
