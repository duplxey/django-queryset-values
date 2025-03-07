from django.urls import path

from estates.views import property_list_view, property_detail_view, \
    property_amenities_view

urlpatterns = [
    path("", property_list_view, name="estates-list"),
    path("<int:id>/", property_detail_view, name="estates-detail"),
    path("<int:id>/amenities/", property_amenities_view, name="estates-short-detail"),
]
