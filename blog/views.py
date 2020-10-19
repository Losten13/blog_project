from django.views.generic import ListView, DetailView

from .models import Snippet


class SnippetFeedView(ListView):
    model = Snippet

    # def get_queryset(self):
    #     return self.model.objects.filter(creator_id=self.request.user.id).order_by('-id')




class SnippetDetailView(DetailView):
    model = Snippet
