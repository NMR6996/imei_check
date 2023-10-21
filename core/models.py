from django.utils import timezone
from django.db import models

import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.db.models.signals import post_save
from django.dispatch import receiver


class Phones(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    imei = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default="Qedyiyyatdan keçirilməyib!")

    def __str__(self):
        return self.brand

@receiver(post_save, sender=Phones)
def update_status(sender, instance, **kwargs):
    if not instance.status == "Qeydiyyatdan keçib!":
        return instance
    print(f"send an email func called! in{sender}, {instance}")
    return instance