# Generated by Django 4.2.11 on 2025-03-31 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Название')),
                ('author_last_name', models.CharField(max_length=50, verbose_name='Название')),
                ('author_middle_name', models.CharField(max_length=50, verbose_name='Название')),
                ('other_authors', models.TextField(blank=True, null=True, verbose_name='Имена соавторов')),
            ],
            options={
                'verbose_name': 'Автора',
                'verbose_name_plural': 'Имена всех авторов',
                'db_table': 'AuthorNames',
            },
        ),
        migrations.CreateModel(
            name='TypesOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(unique=True, verbose_name='Тип публикации')),
            ],
            options={
                'verbose_name': 'Тип научной работы',
                'verbose_name_plural': 'Типы научных работ',
                'db_table': 'TypesOfWorks',
            },
        ),
        migrations.CreateModel(
            name='IntelForScienceWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('annotation', models.TextField(blank=True, null=True, verbose_name='Аннотация')),
                ('OECD', models.CharField(max_length=250, verbose_name='OECD')),
                ('key_words', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ключевые слова')),
                ('year_publication', models.IntegerField(verbose_name='Год публикации')),
                ('work_type_name', models.CharField(max_length=300, verbose_name='Название источника')),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.authornames', verbose_name='Авторы')),
                ('type_of_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.typesofwork', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Информация о научной работе',
                'verbose_name_plural': 'Информация о научных работах',
                'db_table': 'ScienceData',
            },
        ),
    ]
