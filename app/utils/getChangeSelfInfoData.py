import os
from app.models import User
from django.conf import settings


def changeSelfInfo(username, formData, file):
    user = User.objects.get(username=username)
    user.address = formData["address"]
    user.sex = formData["sex"]
    if formData.get("textarea", None):
        user.textarea = formData["textarea"]

        # 处理文件上传（仅当上传了头像文件时才处理）
    avatar_file = file.get('avatar')
    if avatar_file:
        # 校验文件类型和大小
        if avatar_file.content_type not in ['image/jpeg', 'image/png']:
            raise ValueError("仅支持 JPEG 和 PNG 格式的图片")
        if avatar_file.size > 2 * 1024 * 1024:
            raise ValueError("文件大小不能超过 2MB")

        # 确定文件保存路径
        avatar_path = os.path.join('avatar/', avatar_file.name)
        full_avatar_path = os.path.join(settings.MEDIA_ROOT, avatar_path)

        # 保存文件到媒体目录
        with open(full_avatar_path, 'wb+') as destination:
            for chunk in avatar_file.chunks():
                destination.write(chunk)

        # 更新用户头像字段
        user.avatar = avatar_path

    # 保存用户信息
    user.save()

    # ##处理文件上传
    # ##处理头像上传
    # if file.get('avatar') is not None:
    #     avatar_file = file.get('avatar')
    #
    # # 检查avatar_file是否存在
    #
    # if not avatar_file:
    #     raise ValueError("No avatar file provided.")
    #
    # # 校验文件类型和大小
    # if avatar_file.content_type not in ['image/jpeg', 'image/png']:
    #     raise ValueError("仅支持 JPEG 和 PNG 格式的图片")
    # if avatar_file.size > 2 * 1024 * 1024:
    #     raise ValueError("文件大小不能超过 2MB")
    #
    # # 确定文件保存路径
    #
    # avatar_path = os.path.join('avatar/', avatar_file.name)
    # full_avatar_path = os.path.join(settings.MEDIA_ROOT, avatar_path)
    #
    # # 保存文件到媒体目录
    # with open(full_avatar_path, 'wb+') as destination:
    #     for chunk in avatar_file.chunks():
    #         destination.write(chunk)
    #
    # # 更新用户头像字段
    # user.avatar = avatar_path
    #
    # # 保存用户信息
    # user.save()

def getChangePassword(userInfo, passwordInfo):
    oldPwd = passwordInfo['oldPassword']
    newPwd = passwordInfo['newPassword']
    newPwdConfirm = passwordInfo['newPasswordConfirm']
    user = User.objects.get(username=userInfo.username)
    if oldPwd != userInfo.password:
        return "原始密码错误"
    if newPwd != newPwdConfirm:
        return "两次密码不一致"
    user.password = newPwd
    user.save()