from django.db import models

class PaidBooksCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/paidpdfcategory/')

    def __str__(self):
        return self.name


class PaidBooksSubcategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField('uploads/paidpdfsubcat/')
    paidbookscategory = models.ForeignKey(PaidBooksCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PaidBooks(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/paidpdfimage/')
    paidpdf = models.FileField(upload_to='uploads/paidpdfbooks')
    description = models.CharField(max_length=1000)
    paidbookssubcategory = models.ForeignKey(PaidBooksSubcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title and self.paidbookssubcategory


class FreeBooks(models.Model):
    title = models.CharField(max_length=50)
    freepdf = models.FileField(upload_to='uploads/freepdfbooks/')
    image = models.ImageField(upload_to='uploads/freepdfimage/')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title



