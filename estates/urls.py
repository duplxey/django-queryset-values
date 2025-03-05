from django.urls import path

from estates.views import properties_list_view, properties_detail_view

urlpatterns = [
    path("", properties_list_view, name="estates-list"),
    path("<int:id>/", properties_detail_view, name="estates-detail"),
]
