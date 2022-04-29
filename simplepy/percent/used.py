class used():
    def __init__(self):
        pass
    
    def start(used, total, output=None):
        used_percent = (int(used)/int(total))*100
        if output == str:
            used_percent = str(round(used_percent))
        if output == int:
            used_percent = int(round(used_percent))
        return used_percent