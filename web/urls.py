from django.urls import path, include
from web.views import index, subscribe, contact, product


app_name = "web"

urlpatterns = [
    path("", index, name = "index"),
    path("subscribe/", subscribe, name="subscribe"),
    path("contact/", contact, name="contact"),
    path("product/<int:pk>/", product, name="product")
]
