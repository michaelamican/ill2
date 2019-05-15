from django.db import models

# Create your models here.

class Admin(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length = 255)
	username = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Business(models.Model):
	shipping_address = models.TextField(max_length = 2000)
	billing_address = models.TextField(max_length = 2000)
	orders_fulfilled = models.BooleanField(null=False)
	total_spending = models.IntegerField()
	primary_contact = models.CharField(max_length = 255)
	phone = models.TextField(max_length=255)
	email = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Client(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length = 255)
	business_id = models.ForeignKey(Business, on_delete = models.PROTECT)
	password = models.CharField(max_length = 255)
	total_purchase = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Product(models.Model):
	material = models.CharField(max_length = 255)
	color = models.CharField(max_length = 255)
	design = models.CharField(max_length = 255)
	scope = models.TextField(max_length = 2000)
	price_by_yard = models.PositiveIntegerField()
	emboss = models.BooleanField(null=False)
	engrave = models.BooleanField(null=False)
	laser_cut = models.BooleanField(null=False)
	embed = models.BooleanField(null=False)
	embroider = models.BooleanField(null=False)
	heat_treatment = models.BooleanField(null=False)
	glass = models.BooleanField(null=False)
	paint = models.BooleanField(null=False)
	etch = models.BooleanField(null=False)
	other_treatment = models.CharField(max_length=255, default = 'None')
	picture = models.ImageField(null=False)
	product_description = models.TextField(max_length = 2000)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Vendor(models.Model):
	name = models.CharField(max_length = 255)
	service = models.CharField(max_length = 255)
	business_id = models.ForeignKey(Business, on_delete = models.CASCADE)
	total_business = models.ForeignKey(Product, related_name='vendor_sales', on_delete=models.PROTECT)
	partnerships = models.ForeignKey(Business, related_name='preferred_partner', on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Order(models.Model):
	client_name = models.ForeignKey(Client, related_name = 'client_order', on_delete = models.CASCADE)
	current_supplier = models.ForeignKey(Vendor, related_name = 'fulfillment', on_delete = models.PROTECT)
	quantity = models.IntegerField()
	item = models.ForeignKey(Product, on_delete= models.CASCADE)
	price = models.IntegerField()
	completed = models.BooleanField(null=False)
	location = models.ForeignKey(Business, related_name='current_status', on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

