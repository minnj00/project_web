# Generated by Django 5.0 on 2023-12-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_recipedetail_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipedetail',
            name='step',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipeingred',
            name='amount',
            field=models.CharField(max_length=50),
        ),
    ]
