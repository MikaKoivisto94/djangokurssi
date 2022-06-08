from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length= 50, default="Company")
    contactname = models.CharField(max_length= 50, default="Contact")
    address = models.CharField(max_length= 100, default="Address")
    phone = models.CharField(max_length= 20, default="Phone")
    email = models.CharField(max_length= 50, default="Email")
    country = models.CharField(max_length= 50, default="Country")
    # Allaolevan voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length= 20, default="Product")
    packagesize = models.CharField(max_length= 20, default= 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default= 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # Allaolevan voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
