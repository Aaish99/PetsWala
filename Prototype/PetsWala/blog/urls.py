from django.urls import path
from . import views
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
urlpatterns = [
    path('', views.home, name='index'),
    path('blog', BlogPostListView.as_view(), name='blog-home'),
    path('add_new_post/', BlogPostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('blog/post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact_us, name='blog-contact-us'),
    
]
