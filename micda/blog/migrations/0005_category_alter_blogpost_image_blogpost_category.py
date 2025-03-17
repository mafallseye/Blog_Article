# Generated by Django 5.1.6 on 2025-03-17 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogpost_description_remove_blogpost_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
