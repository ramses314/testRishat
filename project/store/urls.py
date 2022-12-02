from django.urls import path
from .views import *

app_name = 'store'
urlpatterns = [
    path('', home, name='home'),

    # API request
    path('buy/<int:id>/', ProductBuyView.as_view(), name='buy_item'),
    path('item/<int:id>/', ProductView.as_view(), name='get_item'),

    # After Pay
    path('success/', SuccessView.as_view(), name='success_payment'),
    path('cancel/', CancelView.as_view(), name='failed_payment'),
]
