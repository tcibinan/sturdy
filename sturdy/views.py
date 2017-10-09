from django.views.generic import TemplateView
from .models import Project

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'sturdy/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['active_projects'] = Project.objects.all()[:5]
        context['all_projects'] = Project.objects.all()
        return context