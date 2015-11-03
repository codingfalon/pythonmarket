shopping_list = ["banana", "orange", "apple"]  #creates a list of items

stock = {                       #key/value pairs track items/quantities
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {                      #key/value pairs track items/prices          
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):         #creates function to calculate bill       
    total = 0
    for item in food:           #iterates through list, adding price of item based on item amount in each iteration
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1 
    return total                #calls the function, "total" represents the bill 