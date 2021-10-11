import factory
from django.contrib.gis.geos import Point

from parking_permits_app.models import Address


class AddressFactory(factory.django.DjangoModelFactory):
    id = factory.Faker("uuid4")
    street_name = factory.Faker("street_name", locale="fi")
    street_number = factory.Faker("building_number")
    street_name_sv = factory.Faker("street_name", locale="sv")
    city = factory.Faker("city", locale="fi")
    city_sv = factory.Faker("city", locale="sv")
    postal_code = factory.Faker("postcode")
    location = Point(10000, 10000)

    class Meta:
        model = Address