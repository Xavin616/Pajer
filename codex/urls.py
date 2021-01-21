from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.sidebar, name='side'),
    path('head', views.def_headline, name='def_headline'),
    path('sources/headlines<int:id>', views.headline, name='headline'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("sources", views.sources, name="sources"),
    path('delete_source/<int:id>', views.delete, name='delete_source'),
    path('follow_source/<int:id>', views.follow, name='follow_source'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)