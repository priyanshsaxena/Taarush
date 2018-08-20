from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('posts/', views.all_posts, name='allposts'),
    path('categories/', views.all_categories, name='all_categories'),
    path('post/<slug:title>', views.view_post, name='viewpost'),
    path('category/<slug:category>', views.view_category, name='viewcategory'),
    path('contact', views.contact, name='contact'),
    path('newpost', views.post_new, name='post_new'),
    path('signup', views.new_user, name='new_user'),
    # path('welcome', views.new_user, name='new_user'),
    # path('success', views.new_user, name='new_user'),
]