# Generated by Django 3.2.4 on 2021-09-12 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('puticasa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Archived')], default=1)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, 'Guest'), (1, 'Tenant'), (2, 'Admin')], default=0)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='puticasa.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
