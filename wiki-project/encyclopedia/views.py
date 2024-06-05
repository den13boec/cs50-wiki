from django.shortcuts import redirect, render
from django.urls import reverse
from . import util


def index(request):    
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def entry(request, entry_title):
    return render(request, "encyclopedia/entry.html", {"entry_title": entry_title, "entry_content": util.read_entry(entry_title)})

def search_entry(request):
    searched_article = request.GET.get("search_article")
    if searched_article:       
        if entry_text := util.read_entry(searched_article):
            return render(request, "encyclopedia/entry.html", {"entry_title": searched_article, "entry_content": entry_text})            
        else:
            all_articles = util.list_entries()
            all_articles = [art for art in all_articles if searched_article in art]
            return render(request, "encyclopedia/search_results.html", {"entries": all_articles})