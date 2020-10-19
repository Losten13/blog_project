from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from blog.views import SnippetFeedView, SnippetDetailView

urlpatterns = [
    path('feed', SnippetFeedView.as_view(), name='snippet_list'),
    path('snippets/<int:pk>/', login_required(SnippetDetailView.as_view()), name='snippet_detail'),
    path('', include('authentication.urls')),
]

urlpatterns += staticfiles_urlpatterns()
