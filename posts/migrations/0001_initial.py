# Generated by Django 3.2.25 on 2024-03-29 09:55

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Post_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('image', models.ImageField(blank=True, default='../default_post_g5kn5h', upload_to='images/')),
                ('video', models.FileField(blank=True, default='../default_video_waimeh', storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video])),
                ('image_filter', models.CharField(choices=[('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'), ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'), ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'), ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'), ('walden', 'Walden'), ('xpro2', 'X-pro II')], default='normal', max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', tagulous.models.fields.TagField(_set_tag_meta=True, force_lowercase=True, help_text='Enter a comma-separated tag string', max_count=15, to='posts.Tagulous_Post_tags')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
