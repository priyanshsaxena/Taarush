from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from .models import Blog, Category, User
from .form import PostForm, UserForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

# def all_posts(request):   
#     # return render_to_response('view_post.html', {
#     #     'post': get_object_or_404(Blog, slug=slug)
#     # })
#     return render_to_response('all_posts.html', {
#         'category': category,
#         'posts': Category.objects.all()
#     })

def all_categories(request):
    return render_to_response('all_categories.html', {
        'categories': Category.objects.all()
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def contact(request):
    return render_to_response('contact.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user_name
            post.posted = timezone.now()
            post.save()
            post = Blog.objects.get(pk=post.pk)
            return redirect('viewpost', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = make_password(form.cleaned_data['password'])
            user = User(user_name=user_name, password=password)
            user.save()
            request.session['logged_in_user'] = user_name
            request.session.set_expiry(300);
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'new_user.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = User.objects.get(user_name=user_name)
            if(user and check_password(password, user.password)):
                request.session['logged_in_user'] = user_name
                request.session.set_expiry(300);
                return redirect('index')
            else:
                form.add_error('password', 'Incorrect Password')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response