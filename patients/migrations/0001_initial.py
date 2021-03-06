# Generated by Django 3.2.9 on 2021-12-07 20:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=70, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('username', models.CharField(max_length=20, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientsRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('B', 'Binary')], max_length=50)),
                ('address', models.TextField(max_length=255)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('occupation', models.CharField(max_length=200)),
                ('allergies', models.CharField(max_length=255)),
                ('recent_diagnosis', models.CharField(choices=[('ML', 'Malaria'), ('FV', 'Fever'), ('CH', 'Cholera'), ('CA', 'Cancer')], max_length=50)),
                ('sport_participation', models.CharField(choices=[('N', 'No'), ('S', 'Sometimes'), ('Y', 'Always')], max_length=50)),
                ('sleep_routine', models.CharField(max_length=255)),
                ('smoke_drink', models.CharField(choices=[('SM', 'Smokes'), ('DR', 'Drinks'), ('SD', 'Smokes and Drinks'), ('NO', 'None')], max_length=50)),
                ('self_medication', models.CharField(choices=[('N', 'No'), ('Y', 'Always')], max_length=255)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('service', models.CharField(choices=[('O', 'Optical Service'), ('D', 'Dental Service'), ('P', 'Pediatric Service'), ('L', 'Laboratory Service')], max_length=250)),
                ('time', models.CharField(choices=[('8', '8AM TO 10AM'), ('10', '10AM TO 12PM'), ('12', '12PM TO 2PM'), ('2', '2PM TO 4PM'), ('4', '4PM TO 6PM'), ('6', '6PM TO 8PM'), ('5', '4PM TO 10PM'), ('11', '10PM TO 12PM')], max_length=250)),
                ('notes', models.TextField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
