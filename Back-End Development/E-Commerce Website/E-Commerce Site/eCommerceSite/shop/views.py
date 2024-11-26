from django.shortcuts import render
from .models import Product,Order
from django.core.paginator import Paginator
# Create your views here.
 
def index(request):
    product_objects = Product.objects.all()
 
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
 
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'app/index.html',{'product_objects':product_objects})
 
 
def details(request,id):
    product_object = Product.objects.get(id=id)
    return render(request,'app/details.html',{'product_object':product_object})
    
def checkout(request):
 
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
 
    return render(request,'app/checkout.html')