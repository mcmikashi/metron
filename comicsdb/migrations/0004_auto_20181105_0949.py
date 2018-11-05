# Generated by Django 2.1.3 on 2018-11-05 14:49

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comicsdb', '0003_series_type_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credits',
            options={'ordering': [
                'creator__last_name', 'creator__first_name'], 'verbose_name_plural': 'Credits'},
        ),
        migrations.AlterField(
            model_name='arc',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='creator',
            name='birth',
            field=models.DateField(blank=True, null=True,
                                   verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='death',
            field=models.DateField(blank=True, null=True,
                                   verbose_name='Date of Death'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='name',
            field=models.CharField(
                blank=True, max_length=255, verbose_name='Story Title'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='founded',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name='Year Founded'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='image',
            field=sorl.thumbnail.fields.ImageField(
                blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='series',
            name='desc',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='series',
            name='year_began',
            field=models.PositiveSmallIntegerField(verbose_name='Year Began'),
        ),
        migrations.AlterField(
            model_name='series',
            name='year_end',
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name='Year Ended'),
        ),
    ]