#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    
    a = 10
    b = 5

    sum_result = add(a, b)
    difference_result = subtract(a, b)
    product_result = multiply(a, b)
    quotient_result = divide(a, b)

    print("Sum: {}".format(sum_result))
    print("Difference: {}".format(difference_result))
    print("Product: {}".format(product_result))
    print("Quotient: {}".format(quotient_result))
