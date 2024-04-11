from django.shortcuts import render, HttpResponse, redirect
from .models import ProductTable
from .forms import ProductTableForm

# Create your views here.
def insert_product(request):
    product_data = ProductTable.objects.all()
    if request.method == 'POST':
        form = ProductTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AddProduct')
    else:
        form = ProductTableForm()
    return render(request, 'add_product.html', {'form': form, 'product_data':product_data})
