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
    default_storage.save(filename, ContentFile(content.encode()))

def get_entry(title, convert_to_text_page):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        temp_f = default_storage.open(f"entries/{title}.md")
        temp_f = temp_f.read().decode("utf-8")
        if convert_to_text_page:
            return markdown.markdown(temp_f)
        return temp_f
    except FileNotFoundError:
        return None
