# Generated by Django 4.1.6 on 2023-02-19 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='img',
            options={'ordering': ['date'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=64, verbose_name='автор')),
                ('text', models.TextField(verbose_name='текст')),
                ('date', models.TimeField(auto_now_add=True, verbose_name='дата')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='images.img', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-date'],
            },
        ),
    ]