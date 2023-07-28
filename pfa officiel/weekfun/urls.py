"""
URL configuration for weekfun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import URLPattern, path
from store.views import index
from django.conf.urls.static import static
from weekfun import settings
from store.views import (
    index,
    event_detail,
    add_to_cart,
    cart,
    delete_cart,
    search_events,
    category,
    country,
    contact,
    update_quantity,
    remove_from_cart,
    checkout,
    create_event,
    privacy,
    terms,
    support,
    events,
)
from accounts.views import signup, logout_user, login_user

app_name = "accounts"

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("contact/", contact, name="contact"),
    path("checkout/", checkout, name="checkout"),
    path("signup/", signup, name="signup"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("cart/", cart, name="cart"),
    path("update-quantity/<int:order_id>/", update_quantity, name="update-quantity"),
    path("remove-from-cart/<int:order_id>/", remove_from_cart, name="remove-from-cart"),
    path("cart/delete/", delete_cart, name="delete-cart"),
    path("event/<str:slug>/", event_detail, name="event"),
    path("event/<str:slug>/add-to-cart", add_to_cart, name="add_to_cart"),
    path("search/", search_events, name="search_events"),
    path("category/<str:category>/", category, name="category"),
    path("country/<str:country>/", country, name="country"),
    path('create/', create_event, name='create_event'),
    path('events/', events, name='events'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('support/', support, name='support'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
