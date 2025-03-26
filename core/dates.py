from faker import Faker

fake = Faker()


def fake_name() -> str:
    name = fake.name()
    return name
