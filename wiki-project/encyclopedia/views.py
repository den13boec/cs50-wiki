from django.shortcuts import redirect, render
from django.contrib import messages
from . import util
from random import choice


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

def random_page(_):
    all_entries = util.list_entries()
    rnd = choice(all_entries)
    return redirect("encyclopedia:entry", rnd)

def edit_entry(request, entry_title):
    if request.method == "POST":
        edited_entry_title = request.POST.get("edited_entry_title")
        edited_page_content = request.POST.get("edited_page_content")
        if edited_entry_title and edited_page_content:
            util.save_edited_entry(edited_entry_title, edited_page_content, request.session["old_title"])
            return redirect("encyclopedia:entry", edited_entry_title)
    else:
        request.session["old_title"] = entry_title
    return render(request, "encyclopedia/edit_page.html", {"entry_title": entry_title, "entry_content": util.get_entry(entry_title)})
    