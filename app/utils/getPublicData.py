from app.models import User

def getAllSaleInfoMapData():
    users = User.query.all()
    saleInfoMapData = []
    for user in users:
        saleInfoMapData.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'address': user.address,
            'sale': user.sale
        })
    return saleInfoMapData

def getAllUserInfoData():
    return User.objects.all()