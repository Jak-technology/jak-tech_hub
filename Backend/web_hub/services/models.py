from django.db import models


CONTACT_CHOICES = (
    ('email', 'Email'),
    ('phone', 'Phone'),
    ('both', 'Both')
)

INDUSTRY_CHOICES = (
    ('aero', 'Aerospace'),
    ('agric', 'Agriculture'),
    ('auto', 'Automotive'),
    ('bank', 'Banking'),
    ('biotech', 'Biotechnology'),
    ('chem', 'Chemicals'),
    ('const', 'Construction'),
    ('edu', 'Education'),
    ('energy', 'Energy'),
    ('ent', 'Entertainment'),
    ('fashion', 'Fashion'),
    ('finance', 'Financial Services'),
    ('f&b', 'Food and Beverage'),
    ('govt', 'Government'),
    ('health', 'Healthcare'),
    ('hos', 'Hospitality'),
    ('it', 'Information Technology (IT)'),
    ('ins', 'Insurance'),
    ('legal', 'Legal'),
    ('manu', 'Manufacturing'),
    ('media', 'Media'),
    ('mining', 'Mining'),
    ('pharm', 'Pharmaceuticals'),
    ('real', 'Real Estate'),
    ('retail', 'Retail'),
    ('telecoms', 'Telecommunications'),
    ('transport', 'Transportation'),
    ('tt', 'Travel and Tourism'),
    ('util', 'Utilities'),
    ('who', 'Wholesale'),
    ('others', 'Others'),

)

SERVICE_CHOICES = (
    ('sd', 'Software Development'),
    ('wd', 'Web Development'),
    ('md', 'Mobile App Development'),
    ('it' 'IT Consulting'),
    ('dm', 'Digital Marketing'),
    ('seo', 'Search Engine Optimization (SEO)'),
    ('cm', 'Content Marketing'),
    ('smm', 'Social Media Marketing'),
    ('gd' 'Graphic Design'),
    ('ecomm' 'E-commerce Development'),
   ('ns', ' Network Services'),
)

class Services(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    preferred_contact = models.CharField(
                                         choices=CONTACT_CHOICES,
                                         help_text='Select Preferred Method of Contact'
                                         )
    business_type = models.CharField(choices=INDUSTRY_CHOICES, help_text='Select Your Industry Type')
    service_requested = models.CharField(choice=SERVICE_CHOICES, help_text='Select The Service You want us to do')
    image = models.FileField(upload_to='file_uploads/')
    message = models.TextField()