def my_country(country = "Rwanda"):
    print(f"Hello from {country}")

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer += number
        return answer

def many_multiplied(*numbers):
    multiplied = 1
    for number in numbers:
        multiplied*=number
    return multiplied


def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


        #A function named concatenate_args that takes any number of string 
#arguments in positional arguments format and concatenates them into
# a single string
def concatenate_args(*string_arguments):
    concatenated = ""
    for string in string_arguments:
        concatenated += string
    return concatenated

#A function named concatenate_kwargs that takes any number of string 
# arguments in keyword arguments  format and concatenates them into 
# a single string

def concatenate_kwargs(**kwargs):
    concatenated = ""
    for key,value in kwargs.items():
        concatenated += value
    return concatenated

#The assignment.
