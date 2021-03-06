# Generated by Django 4.0.3 on 2022-04-05 22:20

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
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.CharField(max_length=65)),
                ('neighborhood', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sqft', models.IntegerField()),
                ('main_photo', models.ImageField(blank=True, upload_to='photos/')),
            ],
            options={
                'ordering': ('-price', 'neighborhood'),
            },
        ),
        migrations.CreateModel(
            name='Liveable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
                ('listings', models.ManyToManyField(to='main_app.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Affordability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.CharField(choices=[('low', 'Affordable'), ('medium', 'Wish List'), ('high', 'Over Budget')], default='low', max_length=20)),
                ('liveable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.liveable')),
            ],
            options={
                'ordering': ('budget',),
            },
        ),
    ]
