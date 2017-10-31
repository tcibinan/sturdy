from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from .models import Project, Task
import datetime


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'sturdy/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['active_projects'] = Project.objects.filter(
            created_date__gt=datetime.datetime.now() - datetime.timedelta(days=7))
        context['all_projects'] = Project.objects.all()
        return context


class ProjectMainView(TemplateView):
    template_name = 'sturdy/project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectMainView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=kwargs['project_id'])
        context['correlated_tasks'] = Task.objects.filter(project=kwargs['project_id']).extra(
            order_by=['-value_points', '-story_points'])
        return context


class TaskDetailsView(DetailView):
    template_name = 'sturdy/task_details.html'
    model = Task
    slug_field = 'id'
    slug_url_kwarg = 'task_id'


class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'story_points', 'value_points']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'story_points': NumberInput(attrs={'class': 'form-control'}),
            'value_points': NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Краткое название таски',
            'description': 'Описание',
            'story_points': 'Story points (SP)',
            'value_points': 'Value points (VP)',
        }


class CreateTaskView(CreateView):
    template_name = 'sturdy/task_edit_form.html'
    form_class = TaskEditForm
    model = Task

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['project_id'])
        return super(CreateTaskView, self).form_valid(form)

    def get_success_url(self):
        return reverse('sturdy:project', kwargs={'project_id': self.kwargs['project_id']})


class UpdateTaskView(UpdateView):
    template_name = 'sturdy/task_edit_form.html'
    form_class = TaskEditForm
    model = Task
    slug_field = 'id'
    slug_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse('sturdy:project', kwargs={'project_id': self.kwargs['project_id']})
