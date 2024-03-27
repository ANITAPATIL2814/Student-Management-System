# Generated by Django 5.0.3 on 2024-03-27 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_attendance_subject_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_mark', models.IntegerField()),
                ('exam_mark', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sub')),
            ],
        ),
    ]
