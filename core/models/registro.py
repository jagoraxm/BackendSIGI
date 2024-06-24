from mongoengine import Document, StringField, DateTimeField, signals, BooleanField, ListField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Registro(Document):
    email = StringField(required=True, unique=True)
    active = BooleanField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Registro, self).save(*args, **kwargs)
    

    @classmethod
    def find_one(cls, **kwargs):
        if 'password' in kwargs:
            del kwargs['password']  # Do not use password in these queries
        return cls.objects(**kwargs).first()

def set_update_time(sender, document, **kwargs):  
    document.updated_at = datetime.utcnow()

signals.pre_save.connect(set_update_time, sender=Registro)  # pre_save signal to update timestamp