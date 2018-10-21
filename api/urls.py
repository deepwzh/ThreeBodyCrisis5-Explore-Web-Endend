from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('hp_rank', views.hp_rank_view),
    path('lv_rank', views.lv_rank_view),
    path('lde_rank', views.lde_rank_view),
    path('exp_rank', views.exp_rank_view),
    path('article', views.article_view),
    path('register', views.register_view)
]
