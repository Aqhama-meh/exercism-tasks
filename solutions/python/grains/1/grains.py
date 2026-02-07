def square(number):
    #find if the value is within range
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number -1)
    


def total():
    total_grains = 2 ** 64 - 1 
    return total_grains
                        
