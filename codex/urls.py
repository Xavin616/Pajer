from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.category, name='category'),
    path('list', views.allHeadlines, name='headlines'),
    path('sources', views.sources, name='sources'),
    path('spec-categories/<str:id>', views.categorized_sources, name='categorized-sources'),
    path('sourced/<str:id>', views.source_headlines, name='spec'),
]