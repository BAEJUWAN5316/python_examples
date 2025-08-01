# Generated by Django 5.2.3 on 2025-06-26 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1점'), (2, '2점'), (3, '3점'), (4, '4점'), (5, '5점')], help_text='1점~5점 사이 점수를 주세요')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baemin.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
