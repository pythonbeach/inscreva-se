from django.db import models


class Enrollment(models.Model):

    states = (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins')
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
