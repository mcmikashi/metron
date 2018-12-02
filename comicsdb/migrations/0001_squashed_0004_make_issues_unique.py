# Generated by Django 2.1.3 on 2018-12-02 16:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='arc/%Y/%m/%d/')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('wikipedia', models.CharField(blank=True, max_length=255, verbose_name='Wikipedia Slug')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='character/%Y/%m/%d/')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('wikipedia', models.CharField(blank=True, max_length=255, verbose_name='Wikipedia Slug')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('death', models.DateField(blank=True, null=True, verbose_name='Date of Death')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='creator/%Y/%m/%d/')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Creator')),
            ],
            options={
                'verbose_name_plural': 'Credits',
                'ordering': ['creator__name'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Story Title')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('number', models.CharField(max_length=25)),
                ('cover_date', models.DateField(verbose_name='Cover Date')),
                ('store_date', models.DateField(blank=True, null=True, verbose_name='In Store Date')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='issue/%Y/%m/%d/', verbose_name='Cover')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('arcs', models.ManyToManyField(blank=True, to='comicsdb.Arc')),
                ('characters', models.ManyToManyField(blank=True, to='comicsdb.Character')),
                ('creators', models.ManyToManyField(blank=True, through='comicsdb.Credits', to='comicsdb.Creator')),
            ],
            options={
                'ordering': ['series__name', 'cover_date', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('founded', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Year Founded')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('wikipedia', models.CharField(blank=True, max_length=255, verbose_name='Wikipedia Slug')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='publisher/%Y/%m/%d/', verbose_name='Logo')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('notes', models.TextField(blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sort_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('volume', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('year_began', models.PositiveSmallIntegerField(verbose_name='Year Began')),
                ('year_end', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Year Ended')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Publisher')),
            ],
            options={
                'verbose_name_plural': 'Series',
                'ordering': ['sort_name', 'year_began'],
            },
        ),
        migrations.CreateModel(
            name='SeriesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('wikipedia', models.CharField(blank=True, max_length=255, verbose_name='Wikipedia Slug')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='team/%Y/%m/%d/')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creators', models.ManyToManyField(blank=True, to='comicsdb.Creator')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='variants/%Y/%m/%d/', verbose_name='Variant Cover')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Issue')),
            ],
        ),
        migrations.AddField(
            model_name='series',
            name='series_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.SeriesType'),
        ),
        migrations.AddField(
            model_name='issue',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Series'),
        ),
        migrations.AddField(
            model_name='issue',
            name='teams',
            field=models.ManyToManyField(blank=True, to='comicsdb.Team'),
        ),
        migrations.AddField(
            model_name='credits',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Issue'),
        ),
        migrations.AddField(
            model_name='credits',
            name='role',
            field=models.ManyToManyField(to='comicsdb.Role'),
        ),
        migrations.AddField(
            model_name='character',
            name='creators',
            field=models.ManyToManyField(blank=True, to='comicsdb.Creator'),
        ),
        migrations.AddField(
            model_name='character',
            name='teams',
            field=models.ManyToManyField(blank=True, to='comicsdb.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='credits',
            unique_together={('creator', 'issue')},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['series__sort_name', 'cover_date', 'number']},
        ),
        migrations.AddField(
            model_name='character',
            name='alias',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='credits',
            name='creator',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Creator'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='issue',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Issue'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Creator'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comicsdb.Issue'),
        ),
        migrations.AlterUniqueTogether(
            name='credits',
            unique_together={('issue', 'creator')},
        ),
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together={('series', 'number')},
        ),
    ]
