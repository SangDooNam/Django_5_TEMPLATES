"""Views for the notes app."""
from typing import Any
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from notes.models import notes


def redirect_to_note_detail(request, note_id):
    """Redirect to the note details view."""
    return redirect(reverse("notes:details", args=[note_id]))


def home(request):
    """Home for my notes app."""
    sections_link = reverse("notes:sections")
    details_link = reverse("notes:details", args=[1])
    context = {
                'sections_link': sections_link, 
                'details_link': details_link
                }
    return render(request, "notes/home.html", context)


def _get_section_list_item(text):
    """Return the list item for a section."""
    url = reverse("notes:by_section", args=[text])
    return url


def sections(request):
    """Show the list of note sections."""
    web_frameworks = _get_section_list_item("Web Frameworks")
    setting_up_django = _get_section_list_item("Setting up Django")
    url_mapping = _get_section_list_item("URL Mapping")
    
    context = {
        'web_frameworks': web_frameworks,
        'setting_up_django': setting_up_django,
        'url_mapping' : url_mapping,
    }
    return render(request, "notes/sections.html", context)


class BySection(View):
    def get(self, request, section_name):
        
        lst = [note['text'] for note in notes if note['section'] == section_name]
        sections = reverse('notes:sections')
        context = {
            'lst' : lst,
            'section_name' : section_name,
            'sections' : sections,
        }
        return render(request, 'notes/by_section.html', context)


class SearchResultsView(TemplateView):
    
    template_name = 'notes/search.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        search_term = self.kwargs.get('search_term')
        context['lst'] = [note for note in notes if search_term.lower() in note['text']]
        context['search_term'] = search_term
        return context


class DetailsView(TemplateView):
    template_name = 'notes/details.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        note_id = self.kwargs.get('note_id')
        
        context['num'] = note_id
        context['text'] = notes[note_id - 1]['text']
        context['section'] = notes[note_id - 1]['section']
        n = len(notes)
        context['previous'] = reverse('notes:details', args=[note_id-1 if note_id != 1 else note_id])
        context['next'] = reverse('notes:details', args=[note_id + 1 if note_id != n else note_id])
        
        return context