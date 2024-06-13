from django.shortcuts import redirect, render
from django.contrib import messages
from . import util


def index(request):    
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def entry(request, entry_title):
    return render(request, "encyclopedia/entry.html", {"entry_title": entry_title, "entry_content": util.read_entry(entry_title)})

def search_entry(request):
    if request.method == "GET":
        searched_article = request.GET.get("search_article")
        if searched_article:       
            if entry_text := util.read_entry(searched_article):
                return render(request, "encyclopedia/entry.html", {"entry_title": searched_article, "entry_content": entry_text})            
            else:
                all_articles = util.list_entries()
                all_articles = [art for art in all_articles if searched_article in art]
                return render(request, "encyclopedia/search_results.html", {"entries": all_articles})

def new_page(request):   
    if request.method == "POST":
        entry_title = request.POST.get("entry_title")
        new_page_content = request.POST.get("new_page_content")
        if entry_title and new_page_content:
            res = util.list_entries()
            if entry_title in res:
                messages.warning(request, "Entry already exists")
            else:
                util.save_entry(entry_title, new_page_content)
                return redirect("encyclopedia:entry", entry_title)
    return render(request, "encyclopedia/new_page.html")    
