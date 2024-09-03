def my_decorator(original_func):
    def wrapper():
        print("Something is happening before the function is called")
        original_func()
        print("And something is happening after the function is called")
    return wrapper

@my_decorator
def greeting():
    print("Go get your laptops")

# Call the decorated function
greeting()


