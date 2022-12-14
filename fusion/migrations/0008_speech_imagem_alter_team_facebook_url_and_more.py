# Generated by Django 4.1 on 2022-08-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0007_remove_speech_imagem_team_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='speech/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagran_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
