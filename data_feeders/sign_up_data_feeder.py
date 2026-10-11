from faker import Faker

def sign_up_feeder():
    faker = Faker()
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password(),
    }