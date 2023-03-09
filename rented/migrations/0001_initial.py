# Generated by Django 4.1.7 on 2023-03-09 17:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rented_at', models.DateTimeField(auto_now_add=True)),
                ('devolution_at', models.DateTimeField(null=True)),
                ('book_time', models.DateTimeField()),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copies.copies')),
            ],
        ),
    ]
