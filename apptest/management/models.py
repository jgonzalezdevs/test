from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):

    USER_STATUS = (
        ('active', 'Activo'),
        ('disabled', 'Desactivado'),
        ('locked', 'Bloqueado'),
    )
    rut = models.CharField(max_length=18)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='disabled')
    phone = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        db_table = 'management_users'

class Mortal(User):

    class Meta:
        db_table = 'management_users_mortal'

class Angel(User):

    class Meta:
        db_table = 'management_users_angel'

class GroupType(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    user_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'management_groups_type'

    def __str__(self):
        return "{}-{}".format(self.group.name, self.user_type.name)

class Ticket(models.Model):
    TICKET_STATUS = (
        ('open', 'Abierto'),
        ('pending', 'Pendiente'),
        ('in_process', 'En Proceso'),
        ('resolved', 'Resuelto'),
        ('closed', 'Cerrado'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=TICKET_STATUS, default='disabled')
    start_date = models.DateTimeField(auto_now_add=True)
    
    @property
    def created_time(self):
        from datetime import datetime
        if self.start_date != None:
            then = datetime.now()
        else:
            then = self.start_date
        now  = datetime.now()
        duration = now - then
        hours = int(divmod(duration.total_seconds(), 3600)[0])
        days = int(divmod(duration.total_seconds(), 24)[0])
        return 'Este ticket fue creado hace: {hours} horas / {days} dias.'.format(hours=hours, days=days)
