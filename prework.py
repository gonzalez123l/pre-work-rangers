#write a function to print "Hello_USERNAME"
def hello_name(user_name):
    print(f'Hello {user_name}!')

hello_name('Carlos')

# Question 2 - Print first odd numbers between 1 and 100
def first_odds():
    for number in range(1, 101):
        if number % 2 == 0:
            continue
        else:
            print(number)

first_odds()

#Question 3 - Write a function that returns the max number in a given list
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))

#Question 4 - 
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 - Write a function to return ifthe given year is a leap year a functionreturns the max number in a given list


def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)




# Write a function to check ifall numbers in a list are consecutive
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)
is_consecutive([1,2,3,4,5,6,7,8,9])