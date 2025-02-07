from django.shortcuts import render
from .news_api import get_top_headlines

# List of categories for the filter dropdown
CATEGORIES = [
    ('business', 'Business'),
    ('entertainment', 'Entertainment'),
    ('health', 'Health'),
    ('science', 'Science'),
    ('sports', 'Sports'),
    ('technology', 'Technology'),
]

def home(request):
    category = request.GET.get('category', 'general')  # Default to 'general' if no category is selected
    news_data = get_top_headlines(category=category)
    articles = news_data.get('articles', [])
    
    # Pass the articles and categories to the template
    return render(request, 'news/home.html', {'articles': articles, 'categories': CATEGORIES, 'current_category': category})
