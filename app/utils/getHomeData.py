from app.models import Sales
from django.db.models import Sum, Count

class getHomeData:
    @staticmethod
    def get_highest_consumption_city():
        highest_consumption_city = Sales.objects.values('city').annotate(total_spend=Sum('purchase_amount')).order_by('-total_spend').first()
        return highest_consumption_city

    @staticmethod
    def get_highest_consumption_city_by_total_spend():
        highest_consumption_city_by_total_spend = Sales.objects.values('city').annotate(total_spend=Sum('purchase_amount')).order_by('-total_spend').first()
        return highest_consumption_city_by_total_spend

    @staticmethod
    def get_most_common_product_category():
        most_common_product_category = Sales.objects.values('category').annotate(category_count=Count('category')).order_by('-category_count').first()
        return most_common_product_category