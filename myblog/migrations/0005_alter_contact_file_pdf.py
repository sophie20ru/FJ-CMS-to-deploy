# Generated by Django 4.0.5 on 2022-06-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_contact_file_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='file_pdf',
            field=models.FileField(default=False, upload_to='media/pdfs'),
        ),
    ]
