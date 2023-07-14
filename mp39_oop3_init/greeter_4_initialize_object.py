class Greeter:
    """Greet people in a variety of ways."""

    def initialize_object(self, tone="casual"):
        self.tone = tone

    def say_hello(self):
        if self.tone == "casual":
            print("Hi.")
        elif self.tone == "formal":
            print("Hello.")

greeter = Greeter()
greeter.initialize_object()
greeter.say_hello()