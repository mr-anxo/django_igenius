

from django.urls import path
from blog.views import article, blog


urlpatterns = [
    path("", blog, name="blog"),
    path("article<int:numero_article>/", article, name="article")
]
