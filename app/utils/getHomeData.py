import time
from django.db.models.functions import ExtractYear, ExtractMonth
from app.models import Sales
from django.db.models import Sum, Count


class getHomeData:

    @staticmethod
    def get_highest_consumption_city():
        highest_consumption_city = Sales.objects.values('city').annotate(total_spend=Sum('purchase_amount')).order_by(
            '-total_spend').first()
        return highest_consumption_city

    @staticmethod
    def get_highest_consumption_city_by_total_spend():
        highest_consumption_city_by_total_spend = Sales.objects.values('city').annotate(
            total_spend=Sum('purchase_amount')).order_by('-total_spend').first()
        return highest_consumption_city_by_total_spend

    @staticmethod
    def get_most_common_product_category():
        most_common_product_category = Sales.objects.values('category').annotate(
            category_count=Count('category')).order_by('-category_count').first()
        return most_common_product_category

    @staticmethod
    def get_top_10_cities_by_consumption():
        top_10_cities = Sales.objects.values('city').annotate(
            total_spend=Sum('purchase_amount')
        ).order_by('-total_spend')[:10]
        # 将 Decimal 转换为 float 类型
        for city in top_10_cities:
            city['total_spend'] = float(city['total_spend'])
        return list(top_10_cities)

    @staticmethod
    def get_sales_proportion_by_product_type():
        sales_proportion = Sales.objects.values('category').annotate(total_sales=Sum('purchase_amount')).order_by(
            '-total_sales')
        return sales_proportion

    @staticmethod
    def get_monthly_sales():
        # 同时提取年份和月份
        monthly_sales = Sales.objects.annotate(
            year=ExtractYear('purchase_date'),
            month=ExtractMonth('purchase_date')
        ).values('year', 'month').annotate(
            total_sales=Sum('purchase_amount')
        ).order_by('year', 'month')

        # 格式化为"YYYY-MM"并转换Decimal
        formatted_sales = []
        for sale in monthly_sales:
            formatted_month = f"{sale['year']}-{sale['month']:02d}"  # 补零
            formatted_sales.append({
                'month': formatted_month,
                'total_sales': float(sale['total_sales'])
            })
        return formatted_sales

    @staticmethod
    def getNowTime():
        timeFormat = time.localtime()
        year = timeFormat.tm_year
        month = timeFormat.tm_mon
        day = timeFormat.tm_mday
        return year, month, day
