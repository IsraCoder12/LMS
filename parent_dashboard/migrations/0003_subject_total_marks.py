# Generated by Django 5.1.6 on 2025-03-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_dashboard', '0002_subject_assignment_marks_subject_final_exam_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='total_marks',
            field=models.FloatField(default=0),
        ),
    ]
