# get input as integer 

def get_integer(prompt: str, error_message: str = "") -> int:
     while True:
         try:
             return int(input(prompt))
         except ValueError:
             print(error_message)


#print(get_integer("Please enter an integer: "))

print(get_integer(
    prompt="Enter a value for n: ",
    error_message = "n must be an integer"
))