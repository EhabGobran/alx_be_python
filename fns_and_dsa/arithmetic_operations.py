def perform_operation(num1 ,num2 ,operation):
    match operation :
        case "add":
            res = num1 + num2
        
        case "subtract":
            res = num1 - num2

        case "multiply":
            res = num1 * num2
        
        case "divide":
            if num2 == 0 :
                return "logical erroe dividing by zero"
            res = num1 / num2
    return res
            


