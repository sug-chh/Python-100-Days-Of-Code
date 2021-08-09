import time



def delay_function(function):
    def inner_function():
        time.sleep(5)
        function()
    return inner_function
#Syntactic Sugar
@delay_function
def say_goodbye():
    print("Bye")

#This is how its done in a normal way
inner_function = delay_function(say_goodbye)

inner_function()