from django.db import models


class Enrollment(models.Model):

    states = (
            ('PI', 'Piauí'),
            ('CE', 'Ceará'),
            ('MA', 'Maranhão')
        )
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', unique=True)
    degree = models.CharField('Formação', max_length=100)
    state = models.CharField('Estado', choices=states, max_length=30)
    city = models.CharField('Cidade', max_length=50)
    institution = models.CharField('Instituição', max_length=100)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return self.name
