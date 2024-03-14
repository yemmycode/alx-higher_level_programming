#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    
    a = 10
    b = 5

    print("{a} + {b} = {sum_result}".format(a=a, b=b, sum_result=add(a, b)))
    print("{a} - {b} = {difference_result}".format(a=a, b=b, difference_result=sub(a, b)))
    print("{a} * {b} = {product_result}".format(a=a, b=b, product_result=mul(a, b)))
    print("{a} / {b} = {quotient_result}".format(a=a, b=b, quotient_result=div(a, b)))
