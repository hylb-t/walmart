from app.models import User

def changeSelfInfo(username,formData,file):
    user = User.objects.get(username=username)
    user.address = formData["address"]
    user.sex = formData["sex"]
    if formData.get("textarea", None):
        user.textarea = formData["textarea"]
    if file.get('avatar') != None:
        user.avatar = file.get('avatar')

    user.save()