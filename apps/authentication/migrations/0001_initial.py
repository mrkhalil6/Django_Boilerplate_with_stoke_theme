# Generated by Django 4.1.1 on 2022-09-11 21:51

import apps.authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField(blank=True, null=True)),
                ('org_key', models.TextField(default=apps.authentication.models.create_organization_key)),
                ('status', models.PositiveSmallIntegerField(default=2)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('modified_date', models.DateField(auto_now=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('unique_code', models.CharField(blank=True, max_length=12, null=True)),
                ('secret_token', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user_image', models.ImageField(blank=True, default='media/no_image.png', null=True, upload_to='media/')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('is_organization_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('sort', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, default=2, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_created_by_fk', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_modified_by_fk', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_organization_fk', to='authentication.organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', apps.authentication.models.UserManager()),
            ],
        ),
    ]
