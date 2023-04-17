# Generated by Django 4.1.3 on 2023-03-20 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('mobileno', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=300)),
                ('pincode', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_as', models.CharField(max_length=200)),
                ('source_income', models.CharField(max_length=200)),
                ('total_experience', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='psloan/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, default=None, related_name='bank', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KYCDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('aadharno', models.CharField(max_length=50, unique=True)),
                ('panno', models.CharField(max_length=50, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ITRandTAX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='itrandtax/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='invest/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DematAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dematname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='demat/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='creditline/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('joinfees', models.CharField(max_length=25)),
                ('annualfees', models.CharField(max_length=25)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('offer1', models.CharField(max_length=200, null=True)),
                ('offer2', models.CharField(max_length=200, null=True)),
                ('offer3', models.CharField(max_length=200, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='creaditcard/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('earnupto', models.CharField(max_length=25)),
                ('total_earn', models.CharField(blank=True, max_length=50)),
                ('total_lead', models.CharField(blank=True, max_length=50)),
                ('toatl_sale', models.CharField(blank=True, max_length=50)),
                ('details', models.JSONField(blank=True, null=True)),
                ('training', models.JSONField(blank=True, null=True)),
                ('marketing', models.JSONField(blank=True, null=True)),
                ('banklogo', models.FileField(blank=True, upload_to='bank/')),
                ('active_status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]