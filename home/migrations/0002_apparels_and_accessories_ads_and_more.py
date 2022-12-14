# Generated by Django 4.0 on 2022-06-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparels_and_Accessories_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Electronics_TVs_and_More_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('No_of_Vacency', models.IntegerField()),
                ('Expirey_Date', models.DateField()),
                ('Area', models.TextField()),
                ('city', models.TextField()),
                ('province', models.TextField()),
                ('Salary', models.IntegerField()),
                ('Requirement', models.TextField(max_length=5000)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_and_Accessories_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Real_Estate_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('For Sell', 'For Sell'), ('For Rent', 'For Rent')], max_length=20)),
                ('Furnished', models.CharField(choices=[('Bed', 'Bed'), ('Dinning Table', 'Dinning Table'), ('Sofa', 'Sofa'), ('Chair', 'Chair'), ('Table', 'Table'), ('Daraz', 'Daraz')], max_length=20)),
                ('Bhk', models.IntegerField()),
                ('Square_feet', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Stationery_items_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('model', models.CharField(max_length=122)),
                ('year', models.DateField()),
                ('km_Driven', models.IntegerField()),
                ('Description', models.TextField(max_length=5000)),
                ('Condition', models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New'), ('Likely New', 'Likely New'), ('Not Working', 'Not Working')], max_length=20)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'db_table': 'Sub Category',
            },
        ),
    ]
