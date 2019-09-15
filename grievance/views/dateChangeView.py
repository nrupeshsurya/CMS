import os
from django.conf import settings
from django.views import generic

BASE_DIR = settings.BASE_DIR


class updateLastSubmissionDate(generic.TemplateView):

	def post(self, request, *args, **kwargs):
		newDate = request.POST.get("date")
		jsFile = os.path.join(BASE_DIR, 'grievance/static/grievance/js/date.js')
		with open(jsFile, mode='w') as file:
			file.write("var date=\""+newDate+"\";")
