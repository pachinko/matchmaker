"""forms of questions"""
# -*- coding: utf-8 -*-
from django import forms

LEVELS = {
    ('Mandatory', 'Mandatory'),
    ('Very Important', 'Very Important'),
    ('Somewhat Important', 'Somewhat Important'),
    ('Not Important', 'Not Important'),
}

class UserResponseXXXX(forms.Form):
    """handing the user reponses"""
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
    coworker_answer_id = forms.IntegerField()
    importance_level = forms.ChoiceField(choices=LEVELS)
    coworker_importance_level = forms.ChoiceField(choices=LEVELS)
    



