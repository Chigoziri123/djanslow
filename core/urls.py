from django.urls import path
from core.views import index_view, AddCustomerView

urlpatterns=[
    path('', index_view, name='home'),
    path('add_customer', AddCustomerView.as_view(), name='add')
]