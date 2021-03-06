# Generated by Django 3.1 on 2021-02-25 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(unique='categories')),
                ('cover_image', models.ImageField(upload_to='listings/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upadated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.category')),
            ],
        ),
    ]
