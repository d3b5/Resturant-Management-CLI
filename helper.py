def name_validator(txt):
    if txt.strip()=='':
        return False
    for char in txt.strip():
        if '0'<=char<='9':
            return False
    return True

def int_validator(x):
    return isinstance(x,int) and x>0
def float_validator(x):
    return isinstance(x,float) and x>0


def get_input(prompt, cast_func=str, validator=None, error_message="Invalid Input"):
    while True:
        try:
            val = cast_func(input(prompt))
            if validator and not validator(val):
                raise ValueError
            return val
        except ValueError:
            print(error_message)