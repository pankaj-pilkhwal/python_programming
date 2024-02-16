def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello guys")
        fx(*args, **kwargs)
        print("Thank you for using this system")
    return mfx


@greet
def add_two_numbers(x, y):
    print(x + y)


add_two_numbers(10, 20)
