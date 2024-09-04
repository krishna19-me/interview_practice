def smart_div(func):
    print("Inside smart_div")
    def inner_div(a, b):
        print("inside inner div")
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner_div


@smart_div
def div(a, b):
    print("Calling div")
    return a/b


print(div(2, 5))


# Decorators allows to wrap another function i.e adding an extra feature to an existing function
# Without actually modifying the existing function
