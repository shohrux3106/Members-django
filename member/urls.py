from django.urls import path
from .views import hello, add, addrecord, delete, update, updaterecord

urlpatterns = [
    path('', hello, name="hello"),
    path('add/', add, name="add"),
    path('add/addrecord/', addrecord, name="addrecord"),
    path("delete/<int:id>/", delete, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
]
