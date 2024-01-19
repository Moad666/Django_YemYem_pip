# Generated by Django 4.1.7 on 2023-12-26 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rc.recipe')),
            ],
        ),
    ]
