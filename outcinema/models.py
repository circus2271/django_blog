from django.db import models

# Create your models here.
class Film(models.Model):
# 	tag
	title = models.CharField(max_length=60)
# 	showtime
	start_date = models.DateField()
	short_description = models.TextField(max_length=155)
	description = models.TextField(max_length=990)
# 	author
# 	country сделать отдельной моделью, а пока что оставить строкой
	country = models.TextField(max_length=40)
# 	year
	running_time = models.IntegerField()
# 	genre
# 	screenshots
	slider_image = models.ImageField(upload_to='films')
	detail_page_top_image = models.ImageField(upload_to='films')

class HomepageSlider(models.Model):
	pass

class Slide(models.Model):
	film = models.ForeignKey(Film, on_delete=models.RESTRICT)
	slider = models.ForeignKey(HomepageSlider, on_delete=models.RESTRICT, related_name='slides')
