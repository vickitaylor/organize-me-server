from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ItemDetail(models.Model):
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="detail_item")
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="room")
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    purchased_from = models.CharField(max_length=55, null=True, blank=True)
    price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(7500.00)], default=0.00)
    status = models.ForeignKey(
        "Status", on_delete=models.CASCADE, related_name="status", null=True, blank=True)
    serial_num = models.CharField(max_length=55, null=True, blank=True)
    purchase_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    expiration_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    @property
    def exp_date(self):
        return self.expiration_date.strftime("%m/%d/%Y")

    @property
    def purchased_date(self):
        return self.purchase_date.strftime("%m/%d/%Y")

    @property
    def format_price(self):
        return "${:,.2f}".format(self.price)
