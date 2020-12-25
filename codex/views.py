from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Headline, Source, Category
from .serializers import HeadlineSerializer, SourceSerializer, CategorySerializer
# Create your views here.
@api_view(['GET'])
def index(request):
    api_url = {
        'List': 'headlines-list',
        'Category': 'categories',
        'Sources': 'sources',
        'Specific Sources (Categorized)': 'spec-categories/<str:id>',
        'Specific headlines': 'sourced/<str:id>'
    }
    return Response(api_url)

@api_view(['GET'])
def allHeadlines(request):
    headlines = Headline.objects.all().order_by('-pk')
    serializer = HeadlineSerializer(headlines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def source_headlines(request, id):
    source = Source.objects.get(pk=id)
    sourceHeadline = Headline.objects.filter(source=source).order_by('pubDate')
    serializer = HeadlineSerializer(sourceHeadline, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sources(request):
    sources = Source.objects.all()
    serializer = SourceSerializer(sources, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categorized_sources(request, id):
    category = Category.objects.get(pk=id)
    source = Source.objects.filter(category=category)
    serializer = SourceSerializer(source, many=True)
    return Response(serializer.data)