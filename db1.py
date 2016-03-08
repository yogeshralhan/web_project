
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

class input_db(Document):
	# String newFileName = " ";
	# File imageFile = new File("/users/victor/images/image.png");
	# GridFS gfsPhoto = new GridFS(db, "photo");
	# GridFSInputFile gfsFile = gfsPhoto.createFile(imageFile);
	# gfsFile.setFilename(newFileName);
	# gfsFile.save();


    name=StringField(required=True)
    image=StringField(required=True)
    price=StringField(required=True)
    size=StringField(required=True)
    brand=StringField(required=True)
    color=StringField(required=True)

