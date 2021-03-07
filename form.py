from flask_wtf import Form
from wtforms import StringField, BooleanField, HiddenField, TextAreaField, \
    DateTimeField, FileField


class BulletinForm(Form):
    id = HiddenField('id')
    dt = DateTimeField('发布时间', format='%Y-%m-%d %H:%M:S')
    title = StringField('标题')
    content = TextAreaField('详情')
    valid = BooleanField('是否有效')
    source = StringField('来源')
    author = StringField('作者')
    image = FileField('上传图片', validators=[
                      FileAllowed(['jpg', 'png'], 'Images only!')])
