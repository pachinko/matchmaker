# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20170223_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='their_answer',
            field=models.ForeignKey(blank=True, null=True, to='questions.Answer'),
        ),
    ]
