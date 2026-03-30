import re

def errorCheck(cityName):
    if not cityName:
        return "Please enter a city."
    if bool(re.search(r'\d', cityName)): 
        return "City cannot contain numbers."
    if len(cityName) > 100: 
       return "City name too long."
    return None

