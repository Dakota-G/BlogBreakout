from django.urls import path
from . import views

urlpatterns = [
    # handling data
    path('delete_blog/<int:blog_id>', views.delete_blog),
    path('edit_blog/<int:blog_id>', views.edit_blog),
    path('create_blog', views.create_blog),
    path('create_user', views.create_user),
    # render paths 
    path('blogs/edit/<int:blog_id>', views.blog_editor),
    path('blogs/<int:blog_id>', views.one_blog),
    path('blogs', views.all_blogs),
    path('', views.index),
]

