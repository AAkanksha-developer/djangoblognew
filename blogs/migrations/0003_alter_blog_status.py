# Generated by Django 4.2 on 2023-07-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('published', 'published')], default='Draft', max_length=20),
        ),
    ]