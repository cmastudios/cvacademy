# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20160703_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executionstatus',
            name='lesson',
            field=models.ForeignKey(to='learn.Lesson', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='executionstatus',
            name='program',
            field=models.ForeignKey(to='learn.Program', null=True),
            preserve_default=True,
        ),
    ]
