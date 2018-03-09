from django.db import models

from django.urls import reverse


class mugalim(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_work = models.DateField(null=True, blank=True)


    def get_absolute_url(self):

        return reverse('mugalim-detail', args=[str(self.id)])

    def __str__(self):

        return '%s, %s' % (self.last_name, self.first_name)



class student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_lesson = models.DateField(null=True, blank=True)


    def get_absolute_url(self):

        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):

        return '%s, %s' % (self.last_name, self.first_name)
