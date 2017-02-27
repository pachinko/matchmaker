"""question view"""
from django.shortcuts import render, Http404, get_object_or_404
from django.shortcuts import redirect

from .forms import UserResponseXXXX
from .models import Question, Answer, UserAnswer

# Create your views here.
def single(request, id):
	"""single question"""
#	try:
#		instance = Question.objects.get(id=id)
#	except:
#		raise Http404

	if request.user.is_authenticated():
		print(id)

		queryset = Question.objects.all().order_by('-timestamp')
		instance = get_object_or_404(Question, id=id)
#		user_answer = UserAnswer.objects.get(user=request.user, question=instance)

		try:
			user_answer = UserAnswer.objects.get(user=request.user, question=instance)
#			updated_q = True
		except UserAnswer.DoesNotExist:
			user_answer = UserAnswer()
#			updated_q = False
		except UserAnswer.MultipleObjectsReturned:
			user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
#			updated_q = True
		except:
			user_answer = UserAnswer()
#			updated_q = False
		

		form = UserResponseXXXX(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data)
			question_id = form.cleaned_data.get('question_id')

			answer_id = form.cleaned_data.get('answer_id')
			importance_level = form.cleaned_data.get('importance_level')
			
			their_answer_id = form.cleaned_data.get('their_answer_id')
			their_importance_level = form.cleaned_data.get('their_importance_level')

			question_instance = Question.objects.get(id = question_id)
			answer_instance = Answer.objects.get(id = answer_id)

			print(question_instance.text, answer_instance.text)

			
			user_answer.user = request.user
			user_answer.question = question_instance
			user_answer.my_answer = Answer.objects.get(id=answer_id)
			user_answer.my_answer_importance = importance_level

			if their_answer_id != -1:
				their_answer_instance = Answer.objects.get(id = their_answer_id)
				user_answer.their_answer = their_answer_instance
				user_answer.their_importance_level = their_importance_level
			else:
				user_answer.their_importance_level = "Not Important"



			their_answer_instance = Answer.objects.get(id = their_answer_id)
			user_answer.their_answer = their_answer_instance
			user_answer.their_importance_level = their_importance_level
			
			user_answer.save()

#			next_q = Question.objects.filter(text__icontains="the") order_by("?").first()
			next_q = Question.objects.order_by("?").first()
			return redirect("question_single", id=next_q.id)

		context = {
			"form": form,
			"instance": instance,
			"user_answer": user_answer,
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


