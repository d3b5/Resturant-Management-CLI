def get_input(prompt, cast_func=str, validator=None, error_message="Invalid Input"):
    while True:
        try:
            val = cast_func(input(prompt))
            if validator and not validator(value):
                raise ValueError
            return val
        except:
            print(error_message)