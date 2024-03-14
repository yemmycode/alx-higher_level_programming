#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    
    a = 10
    b = 5

    print("{a} + {b} = {sum_result}".format(a=a, b=b, sum_result=add(a, b)))
    print("{a} - {b} = {difference_result}".format(a=a, b=b, difference_result=subtract(a, b)))
    print("{a} * {b} = {product_result}".format(a=a, b=b, product_result=multiply(a, b)))
    print("{a} / {b} = {quotient_result}".format(a=a, b=b, quotient_result=divide(a, b)))
