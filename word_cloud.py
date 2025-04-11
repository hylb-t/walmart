import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from pymysql import *
import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
from app.models import Sales

def getIntroCloudImg(targetImgSrc,resImgSrc):
    pass
