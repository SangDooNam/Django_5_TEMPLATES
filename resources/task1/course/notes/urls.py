"""Notes URL Configuration."""
from django.urls import path

from notes.views import home, sections, BySection, SearchResultsView, DetailsView


app_name = "notes"

urlpatterns = [
    path('', home, name="home"),
    path('sections/', sections, name="sections"),
    path('sections/<section_name>/', BySection.as_view(), name="by_section"),
    path('<int:note_id>/', DetailsView.as_view(), name="details"),
    path('<str:search_term>/', SearchResultsView.as_view(), name="search"),
]
