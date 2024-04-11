from django.shortcuts import render, HttpResponse, redirect
from .forms import CustomerTableForm
from .models import CustomerTable

# Create your views here.
def index(request):
   return render(request, 'index.html')

def create_customer(request):
   c_tb = CustomerTable.objects.all()
    
   if request.method == 'POST':
      form = CustomerTableForm(request.POST)

      if form.is_valid():
         form.save()
         return redirect('AddCustomer')

   form = CustomerTableForm()
   return render(request, 'newCustomer.html', {'form':form, 'c_tb': c_tb})