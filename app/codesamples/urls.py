from django.urls import path, include

from .views import WordLookupView, WordRegexView

urlpatterns = [
    path('dictionary/', WordLookupView.as_view()),
    path('regex/', WordRegexView.as_view()),
]
