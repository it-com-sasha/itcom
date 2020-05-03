from django.db import models


class BaseField(models.Model):
	title = models.CharField('заголовок', max_length=150)
	description = models.TextField('текст', blank=True)
	slug = models.SlugField('чпу', db_index=True, unique=True)

	class Meta:
		abstract = True

	
	def __str__(self):
		return self.title




class Page(BaseField):
	category = models.ManyToManyField('Category', verbose_name='Категория')
	menu = models.ManyToManyField('Menu', verbose_name='Меню')

	class Meta:
		verbose_name = "Страница"
		verbose_name_plural = "Страници"
		


class Category(BaseField):

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"



class Menu(BaseField):
	slug = None
	
	class Meta:
		verbose_name = "Меню"
		verbose_name_plural = "Меню"