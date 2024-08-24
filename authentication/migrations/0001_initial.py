# Generated by Django 5.1 on 2024-08-14 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('ADMIN', 'Administrador'), ('CLIENT', 'Cliente')], default='CLIENT')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='MyUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='authentication.rolemodel')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
