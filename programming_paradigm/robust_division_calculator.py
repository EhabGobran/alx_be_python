def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except:
        return "Error: Please enter numeric values only."
        raise ValueError("Error: Please enter numeric values only.")
    
    if denominator == 0:
        return "Error: Cannot divide by zero."
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
    result = numerator / denominator
    return f"The result of the division is {result}"