# get input as integer 

def get_integer(prompt: str, error_message: str = "") -> int:
     while True:
         try:
             return int(input(prompt))
         except ValueError:
             print(error_message)
#