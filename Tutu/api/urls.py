from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'TripFM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^account/", include("Tutu.api.account.urls")),
    url(r"^img/", include("Tutu.api.img.urls")),
]
