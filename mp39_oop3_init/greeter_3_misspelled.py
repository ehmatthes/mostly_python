class Greeter:
    """Greet people in a variety of ways."""

    def _init__(self, tone="casual"):
        self.tone = tone

    def say_hello(self):
        if self.tone == "casual":
            print("Hi.")
        elif self.tone == "formal":
            print("Hello.")

greeter = Greeter()
greeter.say_hello()

greeter.tone = "formal"
greeter.say_hello()