from django.db import models
import uuid


class Car(models.Model):
    """Car class."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_number = models.CharField(max_length=10)
    passangers = models.IntegerField()
    production_year = models.IntegerField()
    producent = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    electric_or_hybrid = models.BooleanField()

    def __str__(self):
        return self.registration_number

    def get_car(request, self):
        if "motor_info" in request.GET and request.GET["motor_info"] == "true":
            electric_or_hybrid = self.electric_or_hybrid
        else:
            electric_or_hybrid = "No info"

        if "category_info" in request.GET and request.GET["category_info"] == "true":
            category = self.category
        else:
            category = "No info"

        data = {
            "id": self.id,
            "registration_number": self.registration_number,
            "model": self.model,
            "producent": self.producent,
            "production_year": self.production_year,
            "passangers": self.passangers,
            "category": category,
            "electric_or_hybrid": electric_or_hybrid
        }

        return data
