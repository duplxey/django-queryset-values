from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


PROPERTY_TYPE_APARTMENT = "AP"
PROPERTY_TYPE_HOUSE = "HO"
PROPERTY_TYPE_CONDO = "CO"
PROPERTY_TYPE_LAND = "LA"

PROPERTY_TYPES = {
    PROPERTY_TYPE_APARTMENT: "Apartment",
    PROPERTY_TYPE_HOUSE: "House",
    PROPERTY_TYPE_CONDO: "Condo",
    PROPERTY_TYPE_LAND: "Land",
}


class Property(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    square_feet = models.PositiveIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    has_garage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)
    has_basement = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    year_built = models.PositiveIntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "properties"

    @property
    def rooms(self):
        return self.bedrooms + self.bathrooms

    def __str__(self):
        return self.title
