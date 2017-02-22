"""forms of questions"""
# -*- coding: utf-8 -*-
from django import forms
class UserResponseXXXX(forms.Form):
    """handing the user reponses"""
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()


