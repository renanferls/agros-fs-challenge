from django.db import models

# Create your models here.


class Producer(models.Model):
    firstName = models.CharField(verbose_name='Nombres', max_length=200)
    lastName = models.CharField(verbose_name='Apellidos', max_length=200)
    email = models.EmailField(verbose_name="Email")
    phoneNumber = models.CharField(verbose_name='Telefono', max_length=12)
    address = models.CharField(verbose_name='Direccion', max_length=200)
    city = models.CharField(verbose_name='Ciudad', max_length=200)
    state = models.CharField(verbose_name='Departamento', max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'
    
    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Crop(models.Model):
    producerId = models.ForeignKey(Producer, on_delete=models.PROTECT, related_name='producer')
    cropName = models.CharField('Nombre del cultivo', max_length=200)
    plantingDate = models.DateField(verbose_name='Fecha de cultivo')
    harvestingDate = models.DateField(verbose_name='Fecha de cosecha', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.cropName}'
    
    class Meta:
        verbose_name = 'Crop'
        verbose_name_plural = 'Crops'


class CropReports(models.Model):
    cropId = models.ForeignKey(Crop, on_delete=models.PROTECT, related_name='crop')
    producerId = models.ForeignKey(Producer, on_delete=models.PROTECT)
    reportName = models.CharField('Titulo del reporte', max_length=150)
    reportStr = models.TextField("Texto del reporte")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.reportName} | {self.cropId.cropName}'
    
    class Meta:
        verbose_name = 'Crop Report'
        verbose_name_plural = 'Crop Reports'

