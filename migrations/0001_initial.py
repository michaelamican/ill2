# Generated by Django 2.1 on 2018-08-27 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address', models.TextField(max_length=2000)),
                ('billing_address', models.TextField(max_length=2000)),
                ('orders_fulfilled', models.BooleanField()),
                ('total_spending', models.IntegerField()),
                ('primary_contact', models.CharField(max_length=255)),
                ('phone', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('total_purchase', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='illuminare.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to='illuminare.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('design', models.CharField(max_length=255)),
                ('scope', models.TextField(max_length=2000)),
                ('price_by_yard', models.PositiveIntegerField()),
                ('emboss', models.BooleanField()),
                ('engrave', models.BooleanField()),
                ('laser_cut', models.BooleanField()),
                ('embed', models.BooleanField()),
                ('embroider', models.BooleanField()),
                ('heat_treatment', models.BooleanField()),
                ('glass', models.BooleanField()),
                ('paint', models.BooleanField()),
                ('etch', models.BooleanField()),
                ('other_treatment', models.CharField(default='None', max_length=255)),
                ('picture', models.ImageField(upload_to='')),
                ('product_description', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='illuminare.Business')),
                ('partnerships', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='preferred_partner', to='illuminare.Business')),
                ('total_business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vendor_sales', to='illuminare.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='current_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fulfillment', to='illuminare.Vendor'),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='illuminare.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_status', to='illuminare.Business'),
        ),
    ]
