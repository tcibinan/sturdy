from django.conf.urls import url

from .views import \
    SturdyLoginView, SturdyLogoutView, \
    HomePageView, ProjectMainView, ProjectGanttChartView, \
    TaskDetailsView, CreateTaskView, UpdateTaskView

app_name = 'sturdy'
urlpatterns = [
    url(r'^login$', SturdyLoginView.as_view(), name='login'),
    url(r'^logout$', SturdyLogoutView.as_view(), name='logout'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^project/(?P<project_id>[0-9]+)$', ProjectMainView.as_view(), name='project'),
    url(r'^project/(?P<project_id>[0-9]+)/gantt_chart$', ProjectGanttChartView.as_view(), name='project_gantt_chart'),
    url(r'^project/(?P<project_id>[0-9]+)/task/(?P<task_id>[0-9]+)$', TaskDetailsView.as_view(), name='task_details'),
    url(r'^project/(?P<project_id>[0-9]+)/task/(?P<task_id>[0-9]+)/edit$', UpdateTaskView.as_view(), name='task_edit'),
    url(r'^project/(?P<project_id>[0-9]+)/create_task$', CreateTaskView.as_view(), name='create_task'),
]
