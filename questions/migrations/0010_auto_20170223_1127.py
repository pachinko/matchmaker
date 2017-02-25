# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20170223_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='my_answer',
            field=models.ForeignKey(to='questions.Answer'),
        ),
    ]
