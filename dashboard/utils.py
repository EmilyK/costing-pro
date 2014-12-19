from django.core.exceptions import ValidationError


def check_duplicates(model_name, name, product_size, business_profile):
	check_existing_product = model_name.objects.filter(name=name, product_size=\
		product_size, 
								 	    business_profile=business_profile).count()

	if check_existing_product > 0:
		raise ValidationError("Product already exists, please update inventory instead!")
	return