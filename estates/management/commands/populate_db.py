import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from estates.models import Location, Property, PROPERTY_TYPES


FAKE_COUNT = 5_000


def generate_random_property_name():
    adjectives = [
        "Sunny", "Cozy", "Luxury", "Charming", "Elegant",
        "Modern", "Serene", "Spacious", "Rustic", "Grand",
    ]
    descriptors = [
        "Deluxe", "Classic", "Premium", "Boutique", "Stylish",
        "Exclusive", "Comfortable", "Tranquil", "Opulent", "Scenic",
    ]
    types = [
        "Apartment", "Villa", "Residence", "Loft", "Condo",
        "Penthouse", "Suite", "Cottage", "Manor", "Retreat",
    ]
    return f"{random.choice(adjectives)} {random.choice(descriptors)} {random.choice(types)}"


class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))

        # Create a superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "", "password")

        fake = Faker()

        # Generate fake locations
        locations = [
            Location(
                city=fake.city(),
                state=fake.state(),
                country=fake.country(),
                zip_code=fake.zipcode(),
            )
            for _ in range(FAKE_COUNT)
        ]

        # Bulk create locations
        created_locations = Location.objects.bulk_create(locations)

        # Generate fake properties
        properties = [
            Property(
                title=generate_random_property_name(),
                description=fake.paragraph(),
                property_type=fake.random_element([key for key in PROPERTY_TYPES.keys()]),
                location=location,
                square_feet=fake.random_int(min=500, max=5_000),
                bedrooms=fake.random_int(min=1, max=5),
                bathrooms=fake.random_int(min=1, max=5),
                has_garage=fake.boolean(chance_of_getting_true=50),
                has_balcony=fake.boolean(chance_of_getting_true=50),
                has_basement=fake.boolean(chance_of_getting_true=50),
                has_pool=fake.boolean(chance_of_getting_true=50),
                year_built=fake.year(),
                is_available=fake.boolean(chance_of_getting_true=80),
                price=fake.random_int(min=120_000, max=1_000_000),
            )
            for location in created_locations
        ]

        # Bulk create properties
        Property.objects.bulk_create(properties)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))
