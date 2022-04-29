class percent():        
    def used(used, total, output=None):
        used_percent = (int(used)/int(total))*100
        if output == str:
            used_percent = str(round(used_percent))
        if output == int:
            used_percent = int(round(used_percent))
        return used_percent
    
    def left(left, total):
        left_percent = (int(left)/int(total))*100
        if output == str:
            left_percent = str(round(left_percent))
        if output == int:
            left_percent = int(round(left_percent))
        return left_percent
    
    def lower(number, amount):
        if "%" in amount:
            amount = amount.replace("%", "")
        
        amount = int(amount)/100
        return int(number)*amount
    
    def higher(number, amount):
        if "%" in amount:
            amount = amount.replace("%", "")
            
        amount = int(amount)/100
        amount = amount+1
        return int(number)*amount
