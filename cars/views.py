"""Car view module."""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Car


def list(request):
    """Display all cars."""
    try:
        cars = Car.objects.all()
        data = []
        for car in cars:
            single_car = Car.get_car(request, car)
            data.append(single_car)
    except Exception as e:
        data = {
            "status": "400",
            "message": "Something went wrong.",
            "error": str(e)
        }

    return JsonResponse({"data": data})


def retrive(request):
    """Display single car via id."""
    try:
        id = request.GET["id"]
        car = Car.objects.get(id=id)
        data = Car.get_car(request, car)

    except Exception as e:
        data = {
            "status": "400",
            "message": "Something went wrong.",
            "error": str(e)
        }

    return JsonResponse({"data": data})


@csrf_exempt
def create(request):
    """Create new car."""
    try:
        data = JSONParser().parse(request)
        Car.objects.create(**data)
        data = {
            "status": "201",
            "message": "Car has been added."
        }
    except Exception as e:
        data = {
            "status": "400",
            "message": "Something went wrong.",
            "error": str(e)
        }
    return JsonResponse(data)


@csrf_exempt
def update(request):
    """Update car."""
    try:
        id = request.GET["id"]
        data = JSONParser().parse(request)
        Car.objects.filter(id=id).update(**data)
        data = {
            "status": "200",
            "message": "Car has been updated."
        }
    except Exception as e:
        data = {
            "status": "400",
            "message": "Something went wrong.",
            "error": str(e)
        }
    return JsonResponse(data)


@csrf_exempt
def delete(request):
    """Delete car."""
    try:
        id = request.GET["id"]
        Car.objects.filter(id=id).delete()
        data = {
            "status": "204",
            "message": "Car has been deleted."
        }
    except Exception as e:
        data = {
            "status": "400",
            "message": "Something went wrong.",
            "error": str(e)
        }
    return JsonResponse(data)
