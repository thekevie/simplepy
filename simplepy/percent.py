from .convert import convert

class percent():
    def in_percent(
        number: int,
        string: bool = False,
        round_off: bool = False
    ):
        number = convert(number, to=int)
        x = number / 100
        if round_off is True:
            x = round(x)
        if string is True:
            x = str(x)
        return x



    def used(
        used: int,
        total: int,
        string: bool = False,
        round_off: bool = False
    ):
        used = convert(used, to=int)
        total = convert(total, to=int)
        x = (used / total)*100
        if round_off is True:
            x = round(x)
        if string is True:
            x = str(x)
        return x



    def left(
        left: int,
        total: int,
        string: bool = False,
        round_off: bool = False
    ):
        left = convert(left, to=int)
        total = convert(total, to=int)
        x = (used / total)*100
        if round_off is True:
            x = round(x)
        if string is True:
            x = str(x)
        return x



    def lower(
        number: int,
        amount: int,
        string: bool = False,
        round_off: bool = False
    ):
        if "%" in amount:
            amount = amount.replace("%", "")
        
        number = convert(number, to=int)
        amount = convert(amount, to=int)

        x = number * (amount / 100)
        if round_off is True:
            x = round(x)
        if string is True:
            x = str(x)
        return x


    
    def higher(
        number: int,
        amount: int,
        string: bool = False,
        round_off: bool = False
    ):
        if type(amount) is str:
            if "%" in amount:
                amount = amount.replace("%", "")
        
        number = convert(number, to=int)
        amount = convert(amount, to=int)

        x = number * ((amount / 100) + 1)
        if round_off is True:
            x = round(x)
        if string is True:
            x = str(x)
        return x