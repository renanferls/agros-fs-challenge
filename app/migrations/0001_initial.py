# Generated by Django 4.1.6 on 2023-02-12 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cropName",
                    models.CharField(max_length=200, verbose_name="Nombre del cultivo"),
                ),
                ("plantingDate", models.DateField(verbose_name="Fecha de cultivo")),
                (
                    "harvestingDate",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de cosecha"
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Crop",
                "verbose_name_plural": "Crops",
            },
        ),
        migrations.CreateModel(
            name="Producer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstName", models.CharField(max_length=200, verbose_name="Nombres")),
                (
                    "lastName",
                    models.CharField(max_length=200, verbose_name="Apellidos"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "phoneNumber",
                    models.CharField(max_length=12, verbose_name="Telefono"),
                ),
                ("address", models.CharField(max_length=200, verbose_name="Direccion")),
                ("city", models.CharField(max_length=200, verbose_name="Ciudad")),
                (
                    "state",
                    models.CharField(max_length=200, verbose_name="Departamento"),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Producer",
                "verbose_name_plural": "Producers",
            },
        ),
        migrations.CreateModel(
            name="CropReports",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reportName",
                    models.CharField(max_length=150, verbose_name="Titulo del reporte"),
                ),
                ("reportStr", models.TextField(verbose_name="Texto del reporte")),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "cropId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="crop",
                        to="app.crop",
                    ),
                ),
                (
                    "producerId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.producer"
                    ),
                ),
            ],
            options={
                "verbose_name": "Crop Report",
                "verbose_name_plural": "Crop Reports",
            },
        ),
        migrations.AddField(
            model_name="crop",
            name="producerId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="producer",
                to="app.producer",
            ),
        ),
    ]
