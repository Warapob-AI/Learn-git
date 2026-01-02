def add_plus(num1, num2):
    if isinstance(num1, int): 
        num1 = float(num1) 
    
    if isinstance(num2, int): 
        num2 = float(num2)

    if not isinstance(num1, float) or not isinstance(num2, float):
        return "Error: Both arguments must be float"
    
    return num1 + num2

