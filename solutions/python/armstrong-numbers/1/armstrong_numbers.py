def is_armstrong_number(num):
    # convert into string to get digits better 
    num_str = str(num)
    num_digits = len(num_str)
    
    # calc. sum of digits raised to a power of num_digits
    total = 0
    for digit_char in num_str:
        digit = int(digit_char)
        total += digit ** num_digits
    
    # check if the total is equal to number
    return total == num
