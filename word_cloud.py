import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from app.models import Sales

def generate_city_word_cloud(output_image_path):
    """
    Generates a word cloud image for cities based on sales data.
    """
    # Query city data from the Sales model
    city_data = Sales.objects.values_list('city', flat=True)
    city_text = " ".join(city_data)

    # Generate word cloud
    wordcloud = WordCloud(
        font_path="path_to_font.ttf",  # Specify the font path for Chinese characters
        width=800,
        height=400,
        background_color="white"
    ).generate(city_text)

    # Save the image
    wordcloud.to_file(output_image_path)

def generate_commodity_word_cloud(output_image_path):
    """
    Generates a word cloud image for commodities based on sales data.
    """
    # Query commodity data from the Sales model
    commodity_data = Sales.objects.values_list('commodity', flat=True)
    commodity_text = " ".join(commodity_data)

    # Generate word cloud
    wordcloud = WordCloud(
        font_path="path_to_font.ttf",  # Specify the font path for Chinese characters
        width=800,
        height=400,
        background_color="white"
    ).generate(commodity_text)

    # Save the image
    wordcloud.to_file(output_image_path)