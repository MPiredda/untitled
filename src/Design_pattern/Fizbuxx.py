
# First version
def fizzBuzz(number):
    for i in range(number+1):
        if (i % 3 == 0) & (i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
fizzBuzz(20)

# using function

def fizzBuzz2(number):
    for i in range(number+1):
        fizz = ismultipleof(i, 3)
        buzz = ismultipleof(i, 5)

        if (fizz) & (buzz):
            print("FizzBuzz")
        elif(fizz):
            print("Fizz")
        elif(buzz):
            print("Buzz")
        else:
            print(i)

def ismultipleof(dividend, divider):
    return dividend%divider == 0

fizzBuzz2(29)


#   Third, dictionary

dict = {3:'A',5: 'B', 7: 'C'}
i = 21

def gfb(i, dict, function):
    for d,s in dict.items():
        if function(i,d):
            print((s))
    return

gfb(i,dict,ismultipleof)
gfb(105,dict,ismultipleof)


