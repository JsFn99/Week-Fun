from django.conf import settings
from .forms import EventForm
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import CustomerForm
from store.models import Cart, Event, Order, PromoCode
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order, Cart


# Create your views here.


def index(request):
    event = Event.objects.all()
    return render(request, "store/index.html", context={"event": event})

def events(request):
    event = Event.objects.all()
    return render(request, "store/events.html", context={"event": event})


def event_detail(request, slug):
    event = get_object_or_404(Event, Slug=slug)
    return render(request, "store/detail.html", context={"event": event})


def add_to_cart(request, slug):
    user = request.user
    event = get_object_or_404(Event, Slug=slug)
    cart, _ = Cart.objects.get_or_create(User=user)
    order, created = Order.objects.get_or_create(User=user, 
                                                 Ordered = False,
                                                 Event=event)

    if created:
        cart.Order.add(order)
        cart.save()
    else:
        order.Quantity += 1
        order.save()

    return redirect("cart")


def cart(request):
    cart = get_object_or_404(Cart, User=request.user)
    return render(request, "store/cart.html", context={"orders": cart.Order.all()})


def delete_cart(request):
    if cart := request.user.cart:
    
        cart.delete()
        
    return redirect("index")


def search_events(request):
    query = request.GET.get("q", "")  
    
    events = Event.objects.filter(Name__icontains=query)

    context = {
        "query": query,
        "events": events,
    }

    return render(request, "store/search.html", context)


def category(request, category):
    events = Event.objects.filter(Category=category)
    context = {"events": events, "selected_category": category}
    return render(request, "store/category.html", context)


def country(request, country):
    events = Event.objects.filter(Country=country)
    context = {"events": events, "selected_country": country}
    return render(request, "store/country.html", context)


def contact(request):
    return render(request, "store/contact.html")

def privacy(request):
    return render(request, "store/privacy.html")

def terms(request):
    return render(request, "store/terms.html")

def support(request):
    return render(request, "store/support.html")


def checkout(request):
    cart = Cart.objects.get(User=request.user)
    orders = cart.Order.all()
    total = orders.aggregate(total=Sum(F('Quantity') * F('Event__Lowest_Price')))['total']
    discount = 5
    total -= discount

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            send_order_confirmation_email(customer, customer.email)

            messages.success(request, "Your order has been placed successfully.")
            return redirect('checkout')

    else:
        form = CustomerForm()

    context = {
        'orders': orders,
        'total': total,
        'form': form
    }

    return render(request, 'store/checkout.html', context)


def checkout_view(request):
    promo_code = PromoCode.objects.first()  
    context = {
        'promo_code': promo_code,
       
    }
    return render(request, 'your_template.html', context)

@require_POST
def update_quantity(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    action = request.POST.get("action")

    if action == "reduce":
        order.Quantity -= 1
        if order.Quantity <= 0:
            order.delete()
        else:
            order.save()
    elif action == "increase":
        order.Quantity += 1
        order.save()

    return redirect("cart")


@require_POST
def remove_from_cart(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
                    
    return redirect("cart")


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'store/create.html', {'form': form})

def send_order_confirmation_email(order, customer_email):
    subject = 'Order Confirmation'
    template = 'store/email.html'

    context = {
        'order': order,
    }

    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[customer_email],
        html_message=html_message,
    )
def send_email():
    my_email = ""