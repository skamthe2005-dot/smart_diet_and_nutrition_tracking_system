from django.utils.text import slugify
a="a@gmail.com"
print(slugify(a.split('@')[0]))