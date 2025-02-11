from mongoengine import Document, StringField, DateTimeField, signals, BinaryField, ListField
from datetime import datetime

class Oficios(Document):
    oficio = StringField(required=True, unique=True)
    folio = StringField(required=True)
    fechaOficio = StringField(required=True)
    estatus = StringField(required=True)
    imagen_name = ListField(StringField())
    imagen = ListField(BinaryField())
    imagen_path = ListField(StringField())  # Rutas completas de los archivos
    imagen_historial = ListField(StringField())  # Historial de imágenes
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