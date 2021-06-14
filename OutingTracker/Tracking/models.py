from django.db import models
import os
import numpy as np
from ndarraydjango.fields import NDArrayField


class Encodings(models.Model):
    RegdNo = models.CharField(unique=True, max_length=20)
    #Encoding = models.TextField(max_length=2000)
    Encoding = NDArrayField(shape=(128, ), dtype=np.float64)