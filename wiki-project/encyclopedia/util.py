import re, markdown

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    
def save_edited_entry(title, content, old_title):
    """
    Edits encyclopedia entry
    """
    filename = f"entries/{title}.md"
    old_filename = f"entries/{old_title}.md"
    if default_storage.exists(old_filename):
        default_storage.delete(old_filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None (raw markdown text for edit).
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

# clean text for page
def read_entry(title):
    """
    Retrieves clean text for entry page to show.
    """
    try:
        with open(f"entries/{title}.md", "r", encoding="utf-8") as input_file:
            tempMd = input_file.read()
        return markdown.markdown(tempMd)
    except FileNotFoundError:
        return None
    