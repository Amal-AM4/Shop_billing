from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.forms import formset_factory
from django.db import transaction
from .forms import SalesTableForm, SaleItemTableForm
from .models import SalesTable, SaleItemTable
from product.models import ProductTable

from django.views.decorators.http import require_GET
from django.utils import timezone


@require_GET
def product_search_view(request):
    # Get the user's input from the query parameter 'term'
    search_term = request.GET.get('term', '')

    # You can also get the value of '_type' if needed
    query_type = request.GET.get('_type', '')

    # Get the user's search query from the parameter 'q'
    query = request.GET.get('q', '')

    # Query the products based on the user's search term or query
    products = ProductTable.objects.filter(name__icontains=query)

    # Create a list of dictionaries containing product information
    results = [{'id': str(product.p_id), 'text': product.name} for product in products]

    # Return the results as JSON
    return JsonResponse({'results': results})



# Create your views here.
def get_product_price(request, product_id):
    product = get_object_or_404(ProductTable, pk=product_id)
    data = {'selling_price': str(product.selling_price),
            'qty': int(1)}
    return JsonResponse(data)

def create_sale(request):
    SaleItemFormSet = formset_factory(SaleItemTableForm, extra=1)

    if request.method == 'POST':
        sale_form = SalesTableForm(request.POST)
        sale_item_formset = SaleItemFormSet(request.POST, prefix='sale_item_formset')

        if sale_form.is_valid() and sale_item_formset.is_valid():
            # Save SalesTable
            sale = sale_form.save(commit=False)

            # Set the created_at field before saving
            sale.created_at = timezone.now()

            sale.save()

            # Save SaleItemTable for each form in the formset
            for form in sale_item_formset:
                sale_item = form.save(commit=False)
                sale_item.sales = sale
                sale_item.save()

                # Update product quantity
                product = sale_item.product
                product.unit -= sale_item.qty
                product.save()

            total_taxable_amount = float(request.POST['total-tax-amount-sum'])
            total_tax_amount = 0
            total_disc_amount = float(request.POST['total-discount-amount-sum'])
            total_grand_total = total_taxable_amount - total_disc_amount

            sale.total_taxable_amount = total_taxable_amount
            sale.total_disc_amount = total_disc_amount
            sale.total_grand_total = total_grand_total



            sale.save()

            # Redirect to a success page (replace 'success_page' with the actual URL name)
            return HttpResponse('success_page')
        else:
            # Handle form errors more gracefully, you can log them or display in the template
            print(sale_form.errors)
            print(sale_item_formset.errors)

    else:
        sale_form = SalesTableForm()
        sale_item_formset = SaleItemFormSet(prefix='sale_item_formset')

    context = {
        'sale_form': sale_form,
        'sale_item_formset': sale_item_formset,
    }

    return render(request, 'create_sale.html', context)
