from faker import Faker
from robot.api.deco import keyword

fake = Faker()

class DataGenerator:

    @keyword("Generate Random Username")
    def generate_random_username(self):
        return fake.user_name()

    @keyword("Generate Random Email")
    def generate_random_email(self):
        return fake.email()
