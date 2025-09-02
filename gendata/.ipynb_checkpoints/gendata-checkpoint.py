from faker import Faker

fake = Faker()

# Generate a random name, address, email, etc.
random_name = fake.name()
random_email = fake.email()
random_address = fake.address()

print(random_name, random_email, random_address)