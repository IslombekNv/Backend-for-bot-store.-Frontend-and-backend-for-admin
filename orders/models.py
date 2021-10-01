from django.db import models

from service.models import ServiceModel
from users.models import TelegramUserModel

order = (
    ('Processing', 'Processing'),
    ('Confirmed', 'Confirmed'),
    ('Performing', 'Performing'),
    ('Performed', 'Performed'),
    ('Canceled', 'Canceled'),
)


class OrderModel(models.Model):
    p_id = models.IntegerField()
    user_id = models.IntegerField()
    user = models.CharField(max_length=255)
    product = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    order = models.CharField(max_length=50, choices=order, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

# SEMESTERS = (
#     ('fall', 'Fall'),
#     ('spring', 'Spring')
# )
#
# class YearModel(models.Model):
#     year = models.IntegerField(primary_key=True)
#
#
# class SemesterModel(models.Model):
#     year = models.ForeignKey(YearModel, on_delete=models.PROTECT())
#     title = models.CharField(max_length=100, choices=SEMESTERS)
#
#
# class SubjectModel(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class ProfessorModel(models.Model):
#     title = models.CharField(max_length=100)
#     teaches = models.ManyToManyField(SubjectModel)
#
#
# class MainModel(models.Model):
#     semester = models.ForeignKey(SemesterModel)
#     professor = models.ForeignKey(ProfessorModel)
#     subject = models.ForeignKey(SubjectModel)
#
#
# class StudentModel(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class TakesModel(models.Model):
#     student = models.ForeignKey(StudentModel)
#     subject = models.ForeignKey(SubjectModel)
#     grade = models.IntegerField(null=True, blank=True)
