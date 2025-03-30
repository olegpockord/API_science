from django.db import models


class TypesOfWork(models.Model):

    name = models.CharField(unique=True, blank=False, null=False, verbose_name='Тип публикации')


    class Meta():
        db_table = 'TypesOfWorks'
        verbose_name = 'Тип научной работы'
        verbose_name_plural = 'Типы научных работ'

    def __str__(self):
        return self.name




# Create your models here.
class IntelForScienceWorks(models.Model):

    name = models.CharField(max_length=250, null=False, verbose_name='Название')
    annotation = models.TextField(null=True, blank=True, verbose_name='Аннотация')
    authors =  models.CharField(max_length=250, null=True, verbose_name='Авторы')
    OECD = models.CharField(max_length=250, blank=False, null=False, verbose_name='OECD')
    key_words = models.CharField(max_length=250, blank=True, null=True, verbose_name='Ключевые слова')
    year_publication = models.IntegerField(blank=False, null=False, verbose_name='Год публикации')
    journal_name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название издательства')
    type_of_work = models.ForeignKey(to=TypesOfWork, on_delete=models.CASCADE, verbose_name='Категория')


    class Meta():
            db_table = 'ScienceData'
            verbose_name = 'Информация о научной работе'
            verbose_name_plural = 'Информация о научных работах'


    def __str__(self):
        return self.name
    
    