"""question view"""
from django.shortcuts import render, Http404
from .forms import UserResponseXXXX
from .models import Question, Answer

# Create your views here.
def home(request):
	"""home"""
	if request.user.is_authenticated():
		form = UserResponseXXXX(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data)
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')
# 			question_id = form.cleaned_data.get('answer_id')
#			answer_id = form.cleaned_data.get('question_id')

			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)

			print(question_instance.text, answer_instance.text)
		
		queryset = Question.objects.all().order_by('-timestamp')
#		print(queryset)
		instance = queryset[2]
#		print(instance)
		context = {
			"form": form,
			"instance": instance,
#			"queryset": queryset
		}
		return render(request, "questions/home.html", context)
	else:
		raise Http404


