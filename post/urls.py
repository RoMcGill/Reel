"""
imports
"""
from django.urls import path
from post import views

urlpatterns = [

    path('', views.index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>/', views.PostDetail, name='post-detail'),
    path('tag/<slug:tag_slug>/', views.tags, name='tags'),
    path('<uuid:post_id>/like', views.like, name='like'),
    # path('<uuid:post_id>/solve', views.solve, name='solve'),
    path('<uuid:post_id>/favourite', views.favourite, name='favourite-post'),

]
