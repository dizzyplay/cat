# Generated by Django 2.1.7 on 2019-03-19 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('weight', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('kcal', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cat.Meals'),
        ),
        migrations.AddField(
            model_name='cat',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cat.CatStatus'),
        ),
    ]
