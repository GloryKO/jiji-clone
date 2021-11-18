from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import InterestForm, ProductForm, SignUpForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required


def signup(request):

    ''' function to sign a user up after entering the needed details on the 
    front end and redirect them to the login page 
    '''

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account was successfully created! Now login')
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'jiji/register.html', context)


def user_login(request):

    ''' function to logim  a user up after entering the needed details on the 
    front end and redirect them to the products list page
    '''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.warning(
                        request, 'Error,Check Your Email and Password Combination')
            except:
                messages.warning(
                    request, 'Invalid Login!,Your Email does not exist.')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'jiji/login.html', context)


def user_logout(request):
    ''' 
        function to log a user out of the app
    '''
    logout(request)
    return redirect('products')


@login_required
def products_dashboard(request):

    ''' function to send registered user to their dashboard so they are able to view existing products 
        and also create new products after they have logged in
    '''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                sold = request.POST['is_sold']
                if sold == 'on':
                    sold = True
                else:
                    sold = False
            except:
                sold = False
            product = Product(seller=request.user, name=request.POST['name'], price=request.POST['price'],

                              description=request.POST['description'], image=request.FILES.get('image'), is_sold=sold
                              )
            product.save()
            form = ProductForm()
    else:
        form = ProductForm()
    products = Product.objects.filter(seller=request.user, is_sold=False)
    context = {'products': products, 'form': form}
    return render(request, 'jiji/dashboard.html', context)


def product_list(request):


    ''' function to list out all products to guest users
    '''

    products = Product.objects.filter(is_sold=False)
    context = {'products': products}
    return render(request, 'jiji/products.html', context)


def product_detail(request, product_id):

    
    ''' 
        function to send users to the product detail page. it recieves the
        product id from the url

    '''

    product = Product.objects.get(id=product_id)
    interests = product.interests.all()
    interest = None
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.product = product
            interest.save()
    else:
        form = InterestForm()

    context = {'product': product, 'interests': interests,
               'interest': interest, 'form': form}
    return render(request, 'jiji/product.html', context)


@login_required
def update_product(request, product_id):

    ''' 
        function to update product created by an existing user.
        it makes use of the product id

    '''
    product = Product.objects.get(id=product_id)
    if product.seller == request.user:
        if product.is_sold == True:
            product.is_sold = False
        else:
            product.is_sold = True
        product.save()
        return redirect('products')


@login_required
def delete_product(request, product_id):
    ''' 
        function to delete product created by an existing user.
        it makes use of the product id

    '''
    product = Product.objects.get(id=product_id)
    if product.seller == request.user:
        product.delete()
    return redirect('dashboard')