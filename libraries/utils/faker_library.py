from robot.api.deco import keyword
from faker import Faker

fake = Faker()

class FakerLibrary:

    @keyword
    def random_username(self):
        """Returns a random username"""
        return fake.user_name()

    @keyword
    def random_email(self):
        """Returns a random email"""
        return fake.email()

    @keyword
    def random_password(self):
        """Returns a random password"""
        return fake.password(length=10, special_chars=True)
