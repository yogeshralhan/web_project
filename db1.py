
from mongoengine import *

connect('mylog2')

class registration(Document):
    name_db=StringField(required=True)
    email_db=EmailField(required=True)
    password_db=StringField(required='')
    confirm_password=StringField()



# class Upload(Document):
#     name=EmailField(required=True)
#     file_name=StringField(required=True)
#     #time=DateTimeField(required='')

# class Bookmark_db(Document):
#     name=StringField(required=True)
#     location=StringField(required=True)
#     labels=StringField(required=True)
#     notes=StringField(required=True)
#     email=StringField(required=True)

