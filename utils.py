def find_max(numbers):
    maax=numbers[0]
    for i in numbers:
        if i>maax:
            maax=i
    return maax
