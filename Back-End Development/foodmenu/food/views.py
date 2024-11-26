from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

# def home(request):
#     item_list=Item.objects.all()
#     context={
#         'item_list':item_list,
#     }
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'

# Details
# def details(request,item_id):
#     item=Item.objects.get(pk=item_id)
#     context={
#         'item':item,
#     }
#     return render(request,'food/details.html',context)

class FoodDetail(DetailView):
    model=Item
    template_name='food/details.html'


# create_item
# def create_item(request):
#     form=ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:home')
#     return render(request,'food/item_form.html',{'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image'] 
    template_name = 'food/item_form.html' 
    success_url = '/food/'  

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

# update_item
def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request,'food/item_form.html',{'form':form,'item':item})

def remove_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()  
        return redirect('food:home')  
    return render(request, 'food/remove.html', {'item': item})