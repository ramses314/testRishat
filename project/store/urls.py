from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'store'
urlpatterns = [
    path('', index, name='home'),

    # Stripe urls
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

    # API request
    path('buy/<int:id>/', BuyView.as_view(), name='buy_item'),
    path('item/<int:id>/', ItemView.as_view(), name='get_item'),

    # After Pay
    path('success/', SuccessView.as_view(), name='success_payment'),
    path('cancel/', CancelView.as_view(), name='failed_payment'),
]
