# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20170223_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='their_importance',
            new_name='their_importance_level',
        ),
    ]
