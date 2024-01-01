y = 1
def f(x):
    return x + y;
y = 2
result = f(5)
print(result)

# python has no Closure ?!!
print(f.__closure__)