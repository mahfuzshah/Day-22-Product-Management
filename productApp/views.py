from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoryModel, ProductModel
from .forms import CategoryForm, ProductForm

# Home view: display all products as cards
def home(request):
    products = ProductModel.objects.all()
    return render(request, 'index.html', {'products': products})

# Category views
def category_list(request):
    categories = CategoryModel.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form, 'title': 'Add Category'})

def category_edit(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'title': 'Edit Category'})

def category_delete(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# Product views
def product_list(request):
    products = ProductModel.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'title': 'Add Product'})

def product_edit(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'title': 'Edit Product'})

def product_delete(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# Product detail
def product_detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
