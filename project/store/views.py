import os

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from dotenv import load_dotenv
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Item
import stripe


load_dotenv()

API_SECRET_KEY = os.getenv('STRIPE_PRIVATE_KEY')
API_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')


def home(request):
    products = Item.objects.all()
    context = {
        'products': products,
        'api_key': API_SECRET_KEY,
        'public_key': API_PUBLIC_KEY
    }
    return render(request, 'store/index.html', context=context)


class ProductView(TemplateView):
    template_name = 'store/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, id=self.kwargs['id'])
        context['api_key'] = API_SECRET_KEY
        context['public_key'] = API_PUBLIC_KEY
        return context


class ProductBuyView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Item, id=self.kwargs['id'])
        checkout_session = stripe.checkout.Session.create(
            api_key=API_SECRET_KEY,
            line_items=[
                {
                    'price_data': {
                        'unit_amount': product.price * 100,
                        'currency': product.currency,
                        'product_data': {
                            'name': product.name
                        }
                    },
                    'quantity': 1,
                }
            ],
            payment_method_types=['card'],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/cancel/'
        )
        return Response(data={'sessionId': checkout_session['id'], })


class SuccessView(TemplateView):
    template_name = 'store/success.html'


class CancelView(TemplateView):
    template_name = 'store/cancel.html'