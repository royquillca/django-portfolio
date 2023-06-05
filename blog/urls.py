from django.urls import path

from .views import render_post, render_post_detail



app_name = "blog" # onr sirve para referenciar

urlpatterns = [
    path('', render_post, name="posts"),
    path('<int:post_id>', render_post_detail, name="post_detail")
]

