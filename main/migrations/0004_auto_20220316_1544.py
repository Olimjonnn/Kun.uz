# Generated by Django 3.2.9 on 2022-03-16 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220316_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViderCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=217)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='category_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.vidercategory'),
        ),
    ]
