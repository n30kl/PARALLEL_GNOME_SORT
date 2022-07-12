from os import read
import random
import time
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

@background
def gnomeSort( arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr
 
i =1
while(i == 1):
    arr = []
    length = int(input("Enter array size: "))
    file = open("C:\data\test.txt", "rt")
    data = file.read()
    words = data.split()
    print("num of words: ", len(words))

