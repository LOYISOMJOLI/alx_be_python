def safe_divide(numerator, denominator):
    try:
        #convert inputs to floats
        num = float(numerator)
        deno = float(denominator)

        #perform division
        result = num/deno
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return"Cannot divide by zero."
    except ValueError:
        return "Please enter numeric values only."
