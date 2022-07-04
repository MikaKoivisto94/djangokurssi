"""suppliers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from .views import productlistview, addproduct, deleteproduct, confirmdeleteproduct, edit_product_get
from .views import edit_product_post, supplierlistview, addsupplier, deletesupplier, confirmdeletesupplier, searchsuppliers
from .views import products_filtered, loginview, login_action, logout_action, searchproducts
from .views import customerlistview, addcustomer, confirmdeletecustomer, deletecustomer, searchcustomers
from .views import orderlistview, addorder, confirmdeleteorder, deleteorder, searchorders, edit_supplier_get
from .views import edit_supplier_post, edit_customer_get, edit_customer_post, edit_order_get, edit_order_post
urlpatterns = [

    #Loginview and authentication method
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),
    path('search-products/', searchproducts),

    # Suppliers url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),

    # Customer url's
    path('customers/', customerlistview),
    path('add-customer/', addcustomer),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer),
    path('delete-customer/<int:id>/', deletecustomer),
    path('search-customers/', searchcustomers),
    path('edit-customer-get/<int:id>/', edit_customer_get),
    path('edit-customer-post/<int:id>/', edit_customer_post),

    # Order url's
    path('orders/', orderlistview),
    path('add-order/', addorder),
    path('confirm-delete-order/<int:id>/', confirmdeleteorder),
    path('delete-order/<int:id>/', deleteorder),
    path('search-orders/', searchorders),
    path('edit-order-get/<int:id>/', edit_order_get),
    path('edit-order-post/<int:id>/', edit_order_post),
]
