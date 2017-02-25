"""question view"""
from django.shortcuts import render, Http404, get_object_or_404
from django.shortcuts import redirect

from .forms import UserResponseXXXX
from .models import Question, Answer

# Create your views here.
def single(request, id):
	"""single question"""
#	try:
#		instance = Question.objects.get(id=id)
#	except:
#		raise Http404

	if request.user.is_authenticated():
		print(id)
		form = UserResponseXXXX(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data)
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)
			print(question_instance.text, answer_instance.text)
#			next_q = Question.objects.filter(text__icontains="the") order_by("?").first()
			next_q = Question.objects.order_by("?").first()
			return redirect("question_single", id=next_q.id)



		queryset = Question.objects.all().order_by('-timestamp')
#		instance = queryset[1]
		instance = get_object_or_404(Question, id=id)
		context = {
			"form": form,
			"instance": instance,
#			"queryset": queryset
		}
		return render(request, "questions/single.html", context)
	else:
		raise Http404



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


