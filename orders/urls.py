from django.urls import path

from . import views

urlpatterns = [
    path("order_index", views.order_index, name="order_index"),

    # angle brackets <> captures part of the url and sends as a keyword argument to the view.
    # 'int' limits/changes variable to integer before passing to view
    # order.id is passed in by order_index.html, converted to integer, 
    # named order_id and sent to views.order  
    path("<int:order_id>", views.order, name="order"),

    path("online_order", views.online_order, name="online_order"),
    path("order_confirmation", views.online_order, name="order_confirmation"),
    path("order", views.order, name="order"),
    path("checkout", views.checkout, name="checkout"),
    path("create_order", views.create_order, name="create_order")
]
