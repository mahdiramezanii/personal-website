from django.urls import path
from apps.Blog_app import views

app_name="Blog_app"
urlpatterns=[

    path("",views.ArticleView.as_view(),name="Blog"),
    path("detail/<slug:slug>",views.ArticleDetailView.as_view(),name="Blog-post")

]