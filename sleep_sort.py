# sleepsort: write a function that takes a list of numbers and prints each number n after an n-second delay

import asyncio
import time

## playing with doing it asynchronously; there is no need to sort here
def sleep_sort_async(my_arr):
    tasks = [my_waiter(num) for num in my_arr]
    loop.run_until_complete(asyncio.wait(tasks))

@asyncio.coroutine
def my_waiter(num):
    yield from asyncio.sleep(num)
    print(num)


## synchronous implementation with sort and wait
def sleep_sort(my_arr):
    prev = 0
    for num in sorted(my_arr):
        time.sleep(num-prev)
        prev = num
        print(num)

## synchronous execution
sleep_sort([3, 1, 4])
sleep_sort([3, 3, 3, 1, 4])


## asynchronous execution
loop = asyncio.get_event_loop()
sleep_sort_async([3,1,4])
sleep_sort_async([3, 3, 3,1,4])
loop.close()

