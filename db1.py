
from mongoengine import *

connect('mylog2')

class registration(Document):
    name_db=StringField(required=True)
    email_db=EmailField(required=True)
    password_db=StringField(required=True)
    confirm_password=StringField(required="")
    

    #hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)  # to encryypt password

	#pbkdf2_sha256.verify("password", hash)    # to verify password




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

