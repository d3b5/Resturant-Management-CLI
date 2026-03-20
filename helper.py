def get_input(promt, cast_func=str, validator=None, error_message="Invalid Input"):
    while True:
        try:
            val = cast_func(input(promt))
            if validator and not validator(value):
                raise ValueError
            return val
        except:
            print(error_message)