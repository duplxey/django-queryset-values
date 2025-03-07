from django.http import JsonResponse

from estates.models import Property


def property_list_view(request):
    properties = Property.objects.select_related("location")
    return JsonResponse(
        {
            "count": properties.count(),
            "results": [
                {
                    "id": property.id,
                    "name": property.name,
                    "location": property.location.to_json(),
                    "price": property.price,
                }
                for property in properties
            ],
        }
    )


def property_detail_view(request, id):
    try:
        property = Property.objects.select_related("location").get(id=id)
        return JsonResponse(property.to_json())
    except Property.DoesNotExist:
        return JsonResponse(
            {
                "message": "Property not found!",
            },
            status=404,
        )


def property_amenities_view(request, id):
    try:
        property = Property.objects.get(id=id)
        return JsonResponse({
            "id": property.id,
            "bedrooms": property.bedrooms,
            "bathrooms": property.bathrooms,
            "has_garage": property.has_garage,
            "has_balcony": property.has_balcony,
            "has_basement": property.has_basement,
            "has_pool": property.has_pool,
        })

    except Property.DoesNotExist:
        return JsonResponse(
            {
                "message": "Property not found!",
            },
            status=404,
        )
