from django.urls import path
from blog.views import post_list, post_detail, update, all_post, AboutMePage, share_post, ContactPage, post_search





urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_detail/<int:id>/', post_detail, name='post_detail'),
    path('update/<post_id>/<int:id>/', update, name='update'),
    path('all_post/', all_post, name='all_post'),
    path('about/', AboutMePage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('share/<int:post_id>/', share_post, name='share_post'),
    path('tag/<slug:tag_slug>/', all_post, name='post_list_by_tag'),
    path('search/', post_search, name='post_search'),


]