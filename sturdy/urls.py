from django.conf.urls import url

from .views import HomePageView

app_name = 'sturdy'
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]