# Generated by Django 2.2 on 2019-05-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('0', '보통'), ('1', '중요'), ('2', '매우중요')], default=0, max_length=1)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]