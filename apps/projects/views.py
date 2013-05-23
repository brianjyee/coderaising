from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from .models import Project
from apps.userprofile.models import UserProfile

class ProjectIndexView(ListView):
	model = Project
	template_name="projects/index.html"

###edit view???
class ProjectProposeView(TemplateView):
	pass

class ProjectDetailView(DetailView):
	model = Project
	template_name = "projects/detail.html"
#slug_field = "pk"
#dslug_url_kwarg = "pk"
	def get_context_data(self, **kwargs):
		"This is to print your context variables during testing ONLY"
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		print context
		return context


###edit view???	
class ProjectEditView(UpdateView):
	pass

###should this be a ListView instead with model = UserProfile???
class ProjectUsersView(DetailView):
	model = Project
	template_name = "projects/users.html"

	def get_queryset(self):
		queryset = super(ProjectUsersView,self).get_queryset()

		return queryset
	
	#def get_context_data(self,**kwargs):
	
### ???
class ProjectApplyView(DetailView):
	model = Project
	slug_field="name"
	slug_url_kwarg = "project"

class ProjectApplicantsView(ListView):
	model = UserProfile
