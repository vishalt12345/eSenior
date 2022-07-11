# Generated by Django 4.0.5 on 2022-07-08 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastTimeClicked', models.DateTimeField(auto_now_add=True)),
                ('caregiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_caregiver', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(related_name='Analytics_UserClick', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
