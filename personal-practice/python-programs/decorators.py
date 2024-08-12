def smart_div(func):
    def inner_div(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner_div


@smart_div
def div(a, b):
    return a/b


print(div(2, 5))


# Decorators allows to wrap another function i.e adding an extra feature to an existing function
# Without actually modifying the existing function
