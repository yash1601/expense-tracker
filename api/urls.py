
from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name="overview"),
    path('list/', views.ExpenseList, name="list"),
    path('detail/<str:pk>', views.ExpenseDetail, name="detail"),
    path('create/', views.ExpenseCreate, name="create"),
    path('expense-delete/<str:pk>', views.ExpenseDelete, name="delete")
]