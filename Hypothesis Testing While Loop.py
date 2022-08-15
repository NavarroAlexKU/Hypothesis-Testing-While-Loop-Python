# create number variable
number = round(int(input()))

# set step variable to 0
steps = 0
while number != 1:
    if number < 0:
        # please enter a number bigger than 0:
        print('please enter a number bigger then 0')
        # reset number input:
        number = int(input())
        # add 1 to steps:
        steps+=1
    # check if number is even:
    elif number % 2 == 0:
        # then divide by 2:
        number = number/2
        # round number
        number = round(number,2)
        print(round(number))
        # add 1 to steps:
        steps+=1
    # if odd, evaluate a new number as 3*number+1
    else:
        number = (3*number)+1
        # print number
        print(round(number))
        # add 1 to steps:
        steps+=1
print("steps: ", steps)