# Generated by Django 4.1.7 on 2023-03-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=50)),
                ('matn', models.CharField(max_length=1000)),
                ('sana', models.DateField()),
            ],
        ),
    ]
