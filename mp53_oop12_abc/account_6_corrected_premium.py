from abc import ABC, abstractmethod

class Account(ABC):
    """Model a user account on a site or app."""

    def __init__(self, username, password=""):
        self.username = username
        self._store_password(password)

    def welcome_user(self):
        print(f"Welcome to the site, {self.username}!")

    @abstractmethod
    def close_account(self):
        pass

    def _store_password(self, password):
        print(f"Stored password for {self.username}.")


class FreeAccount(Account):

    def welcome_user(self):
        super().welcome_user()
        print("You'll have limited access on a free account.")
        

class StandardAccount(Account):

    def welcome_user(self):
        super().welcome_user()
        print("You have access to all features on the site.")
        

class PremiumAccount(Account):

    def welcome_user(self):
        super().welcome_user()
        print("Thank you for supporting us at this level!")

    def close_account(self):
        # Query user about exactly what they want.
        # Flag appropriate data for deletion.
        # Flag appropriate data for preservation.
        # Take care of refunds appropriately.
        # Confirm account closure.
        print("We have closed your Premium account.")
        print("  Thank you for your involvement with us.")


if __name__ == "__main__":
    account = PremiumAccount("birdie")
    account.welcome_user()
