from django.shortcuts import render

from crm.forms import OrderForm
from crm.models import Order


# Create your views here.
def first_page(request):
    orders = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {
        'orders': orders,
        'form': form
    })

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    order = Order(order_name=name, order_phone=phone)
    order.save()
    return render(request, 'thanks_page.html', {
        'name': name,
        'phone': phone
    })
