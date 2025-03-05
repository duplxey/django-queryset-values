from django.http import JsonResponse

from estates.models import Property


def properties_list_view(request):
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


def properties_detail_view(request, id):
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
