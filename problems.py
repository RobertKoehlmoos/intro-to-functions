"""
Write a function called list_manipulation. This function should take in four parameters ( a list,
command, location and value).
1. IF the command is 'remove' and the location is 'end', the function should remove the last value
   in the list and return the value removed.
2. IF the command is 'remove' and the location is 'beginning', the function should remove the first value
   in the list and return the value removed.
3. IF the command is 'add' and the location is 'beginning', the function should add the
   value (the 4th parameter) to the beginning of the list and return the list.
4. IF the command is 'add' and the location is 'end', the function should add the
   value (the 4th parameter) to the end of the list and return the list.
5. IF no value is provided to add, it should use 0 as it's value

Example output
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
list_manipulation([1,2,3], "add", "end") #  [1,2,3,0]
"""


def list_manipulation(...):  # three dots is me letting you know to add parameters
    pass


"""
The fibonacci sequence is a sequence of integers. The 0th value is 0, the first is 1.
From there forward, all fibonacci numbers are defined as the sum the the two fibonacci numbers
right before it. So the second number is the sum of the first and zeroth; The 0th and first fibonacci
numbers added together is 0 + 1 = 1, so the second fibonacci number is 1. The third is the second and
first added together, so 1 + 1 = 2 as the third. This patter holds, so the 100th number is the 99th
added to the 98th.

Using recursion, write the below function that, based on a provided integer n, returns the n-th fibonacci number.
Assume the input will be a non-negative integer
"""


def fibonacci(n: int) -> int:
    pass


"""
Tell me what the 100th fibonacci number is. Don't worry, I'll wait.

Okay, I lied, I won't actually wait that long.
You probably noticed your function was taking a while to return. If you wrote your fibonacci function using normal
recursion it probably takes an exponential amount as the number it's calculating grows larger, so caluclating
the 99th fibonacci number takes almost twice as long as the 98th, and four times as long as the 97th, etc.

Rewrite your original function in the below fast_fibonacci to be able to calculate them quickly. Here are some tips:
Your original function repeats work. If I ask for the 100th fibonacci number it will calculate the 99th and 98th numbers,
but in calculating the 99th number it will again calculate the 98th number.  This repetition gets worse the further
down you go.
So take advantage of scoping. First, make some type of data structure that keeps track of fibonacci values you've
already found. Then, using another function you write inside of fast_fibonacci, check if the values you need are already
in that data structure. If not, once you're done calculating then store the number you found for future use.
If you pull it off right you should find that your function runs blazing fast through 1000, which is the highest
number it will be tested against.
If you find it's taking more than a few seconds to test, then hit ctrl-C and figure out what's stopping your code.

This process is called amortization, and the general use of it is a more advanced topic.
"""


def fast_fibonacci(n: int) -> int:
    pass
