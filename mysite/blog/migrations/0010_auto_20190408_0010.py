# Generated by Django 2.2 on 2019-04-07 18:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20190407_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 18, 10, 5, 209349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 18, 10, 5, 210417, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 18, 10, 5, 208206, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='AdFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_favorite', to='blog.Advertisement')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favorite Advertisement',
                'verbose_name_plural': 'Favorite Advertisements',
            },
        ),
    ]
