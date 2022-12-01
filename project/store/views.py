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

API_KEY = os.getenv('STRIPE_PRIVATE_KEY')
PUB_KEY = os.getenv('STRIPE_PUBLIC_KEY')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse(
            {
                "id" : checkout_session.id
            }
        )

def index(request):

    products = Item.objects.all()

    context = {
        'products' : products,
        'api_key' : API_KEY,
        'public_key' : PUB_KEY
    }
    return render(request, 'store/index.html', context=context)




class ItemView(TemplateView):
    template_name = 'store/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, id=self.kwargs['id'])
        context['api_key'] = API_KEY
        context['public_key'] = PUB_KEY
        return context

class BuyView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=self.kwargs['id'])
        checkout_session = stripe.checkout.Session.create(
            api_key=API_KEY,
            line_items=[
                {
                    'price_data': {
                        'unit_amount': item.price * 100,
                        'currency': item.currency,
                        'product_data': {
                            'name': item.name
                        }
                    },
                    'quantity': 1,
                }
            ],
            payment_method_types=['card'],
            mode='payment',
            success_url='http://localhost/success/',
            cancel_url='http://localhost/cancel/'
        )
        return Response(data={'sessionId': checkout_session['id'], })

class SuccessView(TemplateView):
    template_name = 'store/success.html'
class CancelView(TemplateView):
    template_name = 'store/cancel.html'


