"""forms of questions"""
# -*- coding: utf-8 -*-
from django import forms

from .models import LEVELS, Answer, Question

# LEVELS = {
#     ('Mandatory', 'Mandatory'),
#     ('Very Important', 'Very Important'),
#     ('Somewhat Important', 'Somewhat Important'),
#     ('Not Important', 'Not Important'),
# }

class UserResponseXXXX(forms.Form):
    """handing the user reponses"""
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
    their_answer_id = forms.IntegerField()
    importance_level = forms.ChoiceField(choices=LEVELS)
    their_importance_level = forms.ChoiceField(choices=LEVELS)


    def clean_answer_id(self):
        answer_id = self.cleaned_data.get('answer_id')
        try:
            obj = Answer.objects.get(id = answer_id)
        except:
            raise forms.ValidationError('有錯誤 There was an error with the answer. Please try again.')
        return answer_id


    def clean_their_answer_id(self):
        their_answer_id = self.cleaned_data.get('their_answer_id')
        try:
            obj = Answer.objects.get(id = their_answer_id)
        except:
            raise forms.ValidationError('有錯誤 There was an error with their_ answer. Please try again.')
        return their_answer_id


    def clean_question_id(self):
        question_id = self.cleaned_data.get('question_id')
        try:
            obj = Question.objects.get(id = question_id)
        except:
            raise forms.ValidationError('有錯誤 There was an error with the question. Please try again.')
        return question_id




