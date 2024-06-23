from django.urls import path
from . import views

urlpatterns = [
	path("books/<str:id>",views.books),
]