def calc(a,b):
    sum = a+b
    diff = a-b
    mult = a*b
    div = a/b

    results = [sum, diff, mult, div]

    return results

for result in calc(5,10):
    print(result)