from django.shortcuts import render,redirect
from cart.models import Product,Cart,CartItem
from .forms import CreateUserForm,LoginForm
from django.contrib.auth import authenticate,login 
# from .models import CartItem
from django.shortcuts import render
from django.shortcuts import get_object_or_404





def index (request):
    product=Product.objects.all()
    return render (request,'../templates/index.html',{'product':product})

from django.contrib import messages
def bucket(request):
    message = ''
    bucket = None
    if request.method == 'POST':
        user = request.user
        id = request.POST['id']
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        img = request.POST['img']
        

        if Cart.objects.filter(user=user, id=id).exists():
            # bucket already exists
            message = "Already Added"
            messages.warning(request, message)
        else:
            # Create and save the new bucket
            bucket = Cart(user=user, id=id, name=name, category=category, price=price, img=img)
            bucket.save()
            message = "Successfully Added"
            messages.success(request, message)

        return redirect(f'/')
    buckets=Cart.objects.all
    return render(request, "../templates/cart.html", {'message':message,'buckets':buckets})





def search(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(name__icontains=query)  # Adjust this query based on your model fields
    context = {'results': results, 'query': query}
    return render(request, '../templates/search.html', context)

def user_registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'register': form}
    return render(request, '../templates/signup.html', context=context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    context = {'loginform': form}
    return render(request, '../templates/login.html', context=context)

from django.contrib.auth import logout
def user_logout(request):  
    logout(request)
    return redirect("/cart/login")


def delete_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart/')



def add_to_cart(request):
    if request.method == 'POST':
        # Get product details from the form data
        product_id = request.POST.get('id')
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        img = request.POST.get('img')

        # Check if the item is already in the cart
        existing_item = CartItem.objects.filter(id=product_id).first()

        if existing_item:
            # If the item is already in the cart, update the quantity or any other relevant information
            existing_item.quantity += 1  # Update this line based on your actual model structure
            existing_item.save()
        else:
            # If the item is not in the cart, create a new CartItem
            new_item = CartItem.objects.create(
                id=product_id,
                name=name,
                category=category,
                price=price,
                img=img,
            )
            cart_items = CartItem.objects.all()

        # Redirect to the cart page after adding the product
        return redirect('show/')
        return render(request, 'cart.html', {'cart_items': add})

    

def cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})


