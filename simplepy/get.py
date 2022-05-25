def get_type(value, wanted=None):
    if wanted is None:
        return type(value)
    else:
        if type(value) is wanted:
            return True
        else:
            return False