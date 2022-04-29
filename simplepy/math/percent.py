class percent():        
    def used(used, total):
        used_percent = (int(used)/int(total))*100
        return round(used_percent)
    
    def left(left, total):
        left_percent = (int(left)/int(total))*100
        return round(left_percent)
    
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