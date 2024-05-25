###
# Thaw Zin Soe
# thawzinsoe.dev@gmail.com
# 09403077739
###

start = 1 
end = 100
for number in range(start,end):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)