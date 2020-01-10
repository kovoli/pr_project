# Generated by Django 3.0.1 on 2019-12-28 18:52

import ckeditor.fields
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('link_to_shop', models.TextField()),
                ('actual_deal_status', models.BooleanField(default=True)),
                ('status_publish', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, max_length=250, upload_to='category_images/%Y/%m')),
            ],
        ),
    ]
