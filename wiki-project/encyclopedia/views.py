from django.shortcuts import render
from . import util


def index(request):    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_title):
    return render(request, "encyclopedia/entry.html", {"entry_title": entry_title, "entry_content": util.read_entry(entry_title)})