# Generated by Django 4.0.4 on 2022-05-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_descricao_curta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
