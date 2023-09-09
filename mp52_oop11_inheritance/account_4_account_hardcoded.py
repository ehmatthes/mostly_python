class Account:
    """Model a user account on a site or app."""

    def __init__(self, username, password=""):
        self.username = username
        self._store_password(password)

    def welcome_user(self):
        print(f"Welcome to the site, {self.username}!")

    def close_account(self):
        print(f"Closed account for {self.username}.")

    def _store_password(self, password):
        print(f"Stored password for {self.username}.")


class FreeAccount(Account):

    def welcome_user(self):
        Account.welcome_user(self)
        print("You'll have limited access on a free account.")


if __name__ == "__main__":
    account = FreeAccount("eric")
    account.welcome_user()