from django.urls import path
from blog.views import post_list, post_detail, update, all_post



urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('update/<post_id>/<int:id>/', update, name='update'),
    path('all_post/', all_post, name='all_post'),
]