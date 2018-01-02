# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_remove_goodsinfo_isdelete'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
