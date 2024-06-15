from mongoengine import Document, StringField, DateTimeField, signals, BooleanField, ListField
from datetime import datetime

class Notification(Document):
    title = StringField(required=True, unique=True)
    description = StringField(required=True)
    # action = ListField(StringField())
    priority = StringField(required=True)
    active = BooleanField(required=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Notification, self).save(*args, **kwargs)
    

    @classmethod
    def find_one(cls, **kwargs):
        return cls.objects(**kwargs).first()
    
    
def set_update_time(sender, document, **kwargs):  
    document.updated_at = datetime.utcnow()

signals.pre_save.connect(set_update_time, sender=Notification)  # pre_save signal to update timestamp