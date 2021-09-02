def misha_decorator(function):
    def whatever_name(this_is_self):
        print("this is before the function")
        function(this_is_self)
        print("this is the after the function")

    return whatever_name  # you don't run after this, do not add ()


class Apple:

    @misha_decorator
    def eat_apple(self):
        print("yummy apple")


apple = Apple()
apple.eat_apple()
