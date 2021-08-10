from django.urls import path

from .views import *

urlpatterns = [
    path("Daneshkadeh/<str:name>/", dp_view, name="dp_view"),
    path("Professor/posts/all/", all_pp, name="posts-all"),
    path("Professor/all/", professor_all, name="professor-all"),
    path("Professor/post/<str:title>/", professor_post, name="p-post"),
    path("Professor/<str:name>/", prof_detail, name="p_detail"),
]
