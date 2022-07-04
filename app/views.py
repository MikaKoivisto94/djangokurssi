from django.shortcuts import render, redirect
from .models import Supplier, Product, Customer, Order
from django.contrib.auth import authenticate, login, logout

# Landing after login
def landingview(request):
    return render(request, "landingpage.html")

#Login and logout
def loginview(request):
    return render (request, "loginpage.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password= passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request, 'landingpage.html', context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# Product views
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render(request, "productlist.html", context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request, "confirmdelprod.html", context)

def deleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Product.objects.get(id = id).delete()
        return redirect(productlistview)

def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request, "edit_product.html", context)

def edit_product_post(request, id):
    item = Product.objects.get(id = id)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.save()
    return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id) # supplier on foreign key id
    context = {'products': filteredproducts}
    return render (request, "productlist.html", context)

def searchproducts(request):
    search = request.POST['search']
    filtered = Product.objects.filter(productname__icontains=search)
    context = {'products': filtered}
    return render (request,"productlist.html", context)

# Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render(request, "supplierlist.html", context)

def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, "loginpage.html")
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request, "confirmdelsupp.html", context)

def deletesupplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Supplier.objects.get(id = id).delete()
        return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html", context)

def edit_supplier_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request, "edit_supplier.html", context)

def edit_supplier_post(request, id):
    item = Supplier.objects.get(id = id)
    item.contactname = request.POST['contactname']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.address = request.POST['address']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)


# Customer views
def customerlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customerlist = Customer.objects.all()
        context = {'customers': customerlist}
        return render(request, "customerlist.html", context)

def addcustomer(request):
    if not request.user.is_authenticated:
        return render(request, "loginpage.html")
    else:
        a = request.POST['customer']
        b = request.POST['contactname']
        c = request.POST['phone']
        d = request.POST['address']
        e = request.POST['postalcode']
        f = request.POST['city']
        g = request.POST['country']
        Customer(customer = a, contactname = b, phone = c, address = d, postalcode = e, city = f, country = g).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletecustomer(request, id):
    customer = Customer.objects.get(id = id)
    context = {'customer': customer}
    return render (request, "confirmdelcust.html", context)

def deletecustomer(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Customer.objects.get(id = id).delete()
        return redirect(customerlistview)

def searchcustomers(request):
    search = request.POST['search']
    filtered = Customer.objects.filter(customer__icontains=search)
    context = {'customers': filtered}
    return render (request,"customerlist.html", context)

def edit_customer_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customer = Customer.objects.get(id = id)
        context = {'customer': customer}
        return render (request, "edit_customer.html", context)

def edit_customer_post(request, id):
    item = Customer.objects.get(id = id)
    item.contactname = request.POST['contactname']
    item.phone = request.POST['phone']
    item.address = request.POST['address']
    item.postalcode = request.POST['postalcode']
    item.city = request.POST['city']
    item.country = request.POST['country']
    item.save()
    return redirect(customerlistview)


# Order views
def orderlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        orderlist = Order.objects.all()
        customerlist = Customer.objects.all()
        context = {'orders': orderlist, 'customers': customerlist}
        return render(request, "orderlist.html", context)

def addorder(request):
    if not request.user.is_authenticated:
        return render(request, "loginpage.html")
    else:
        a = request.POST['customer']
        b = request.POST['orderdate']
        c = request.POST['freight']
        d = request.POST['shipname']
        e = request.POST['shipaddress']
        f = request.POST['shipcity']
        g = request.POST['country']
        Order(customer = Customer.objects.get(id = a), orderdate = b, freight = c, shipname = d,
        shipaddress = e, shipcity = f, country = g).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeleteorder(request, id):
    order = Order.objects.get(id = id)
    context = {'order': order}
    return render (request, "confirmdelorder.html", context)

def deleteorder(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Order.objects.get(id = id).delete()
        return redirect(orderlistview)

def searchorders(request):
    search = request.POST['search']
    filtered = Order.objects.filter(orderdate__icontains=search)
    context = {'orders': filtered}
    return render (request,"orderlist.html", context)

def edit_order_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        order = Order.objects.get(id = id)
        customerlist = Customer.objects.all()
        context = {'order': order, 'customer': customerlist}
        return render (request, "edit_order.html", context)

def edit_order_post(request, id):
    item = Order.objects.get(id = id)
    item.freight = request.POST['freight']
    item.shipname = request.POST['shipname']
    item.shipaddress = request.POST['shipaddress']
    item.shipcity = request.POST['shipcity']
    item.country = request.POST['country']
    item.save()
    return redirect(orderlistview)