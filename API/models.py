from django.db import models


class TypesOfWork(models.Model):

    type = models.CharField(unique=True, blank=False, null=False, verbose_name='Тип публикации')


    class Meta():
        db_table = 'TypesOfWorks'
        verbose_name = 'Тип научной работы'
        verbose_name_plural = 'Типы научных работ'

    def __str__(self):
        return self.type


class AuthorNames(models.Model):
    author_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    author_last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Фамилия')
    author_middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    other_authors = models.TextField(blank=True, null=True, verbose_name='Имена соавторов')

    class Meta():
        db_table = 'AuthorNames'
        verbose_name = 'Автора'
        verbose_name_plural = 'Имена всех авторов'

    def __str__(self):
        return f"{self.pk} - {self.author_name}"

    def full_author_name(self):
        if self.author_middle_name:
            return f"{self.author_last_name.lower().capitalize()} {self.author_name[0]}. {self.author_middle_name[0]}."
        return f"{self.author_last_name.lower().capitalize()} {self.author_name[0]}."
    

class IntelForScienceWorks(models.Model):

    title = models.CharField(max_length=250, null=False, verbose_name='Название')
    annotation = models.TextField(null=True, blank=True, verbose_name='Аннотация')
    OECD = models.CharField(max_length=250, blank=False, null=False, verbose_name='OECD')
    key_words = models.CharField(max_length=500, blank=True, null=True, verbose_name='Ключевые слова')
    year_publication = models.IntegerField(blank=False, null=False, verbose_name='Год публикации')
    work_type_name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Название источника')
    type_of_work = models.ForeignKey(to=TypesOfWork, on_delete=models.CASCADE, verbose_name='Категория')
    authors = models.ForeignKey(to=AuthorNames, on_delete=models.CASCADE, verbose_name="Авторы")


    class Meta():
            db_table = 'ScienceData'
            verbose_name = 'Информация о научной работе'
            verbose_name_plural = 'Информация о научных работах'


    def __str__(self):
        return f"{self.pk} - {self.title}"
    
