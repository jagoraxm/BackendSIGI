from mongoengine import Document, StringField, DateTimeField, signals
from datetime import datetime

class Oficios(Document):
    oficio = StringField(required=True, unique=True)
    fechaOficio = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Oficios, self).save(*args, **kwargs)
    
    @classmethod
    def find_one(cls, **kwargs):
        return cls.objects(**kwargs).first()
    
    
def set_update_time(sender, document, **kwargs):  
    document.updated_at = datetime.utcnow()

signals.pre_save.connect(set_update_time, sender=Oficios)  # pre_save signal to update timestamp