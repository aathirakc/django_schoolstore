from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from django import forms


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_urls(self):
        return reverse('store_app:products_by_category', args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='courses')

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'
    def __str__(self):
        return self.name

    def get_urls(self):
        return reverse('store_app:course', args=[self.department.slug,self.slug])
# Create your models here.
class Dropdown(models.Model):

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('department')
        password2 = self.cleaned_data.get('course')
        if password1 == None:
            raise ValidationError('Password too short')
        elif password2==None:
            raise forms.ValidationError('passwords do not match')
        return password2





