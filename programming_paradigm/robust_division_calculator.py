def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except:
        raise ValueError("Error: Please enter numeric values only.")
    
    if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
    result = numerator / denominator
    return f"The result of the division is {result}"