from django.urls import path
from . import views
import random
from django.conf import settings
from django.conf.urls.static import static

hey = str(random.randint(100000, 9999999999991))

urlpatterns = [
    path('', views.index1, name='home'),
    path('welcome', views.index, name='index'),
    path('user', views.sidebar, name='side'),
    path('user_landing_page', views.def_headline, name='def_headline'),
    path(f'sources/headlines/<str:id>', views.headline, name='headline'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("sources", views.sources, name="sources"),
    #path("categories", views.categories, name="categories"),
    path("search/", views.search, name='search'),
    path('delete_source/source_feed_number="<int:id>"', views.delete, name='delete_source'),
    path('follow_source/source_feed_name="<str:id>"', views.follow, name='follow_source'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)