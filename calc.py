def calc(a,b):
    sum = a+b
    diff = a-b
    mult = a*b
    div = a/b

    results = [sum, diff, mult, div]

    return results

results = calc(5,10)

for result in results:
    print(result)

print("Sum of results: {}".format(sum(results)))