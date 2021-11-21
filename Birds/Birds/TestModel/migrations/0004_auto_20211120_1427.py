# Generated by Django 3.2.9 on 2021-11-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0003_auto_20211120_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=100)),
                ('address', models.FilePathField()),
                ('link', models.JSONField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Handle',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.RenameField(
            model_name='birdsinfo',
            old_name='pic_id',
            new_name='birdId',
        ),
    ]
