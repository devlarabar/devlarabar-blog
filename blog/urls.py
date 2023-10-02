from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createpost/", views.create_post, name="create_post"),
    path("viewpost/<post_id>/", views.view_post, name="view_post"),
    path("editpost/<post_id>/", views.edit_post, name="edit_post")
]
