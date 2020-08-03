# Generated by Django 3.0.9 on 2020-08-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField()),
                ('comment', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('is_done', models.BooleanField()),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]