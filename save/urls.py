from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import include, path
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    path('Our-Solutions', views.our_Solution, name='solution'),
    path('Who-We-Are/', views.Who, name='who'),
    path('contact-us/', views.contact, name='contact'),
    path('payment-dashboard/', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_request, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)