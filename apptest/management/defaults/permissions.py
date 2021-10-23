"""
 
     _  _     ____                         ___                            _       
   _| || |_  / ___|  ___  _ __ ___   ___  |_ _|_ __ ___  _ __   ___  _ __| |_ ___ 
  |_  ..  _| \___ \ / _ \| '_ ` _ \ / _ \  | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
  |_      _|  ___) | (_) | | | | | |  __/  | || | | | | | |_) | (_) | |  | |_\__ \
    |_||_|   |____/ \___/|_| |_| |_|\___| |___|_| |_| |_| .__/ \___/|_|   \__|___/
                                                        |_|                       
 
"""

from django.contrib.auth.models import Group, ContentType, Permission

"""
 
     _  _      ____          _                    ____                     _         _                 
   _| || |_   / ___|   _ ___| |_ ___  _ __ ___   |  _ \ ___ _ __ _ __ ___ (_)___ ___(_) ___  _ __  ___ 
  |_  ..  _| | |  | | | / __| __/ _ \| '_ ` _ \  | |_) / _ \ '__| '_ ` _ \| / __/ __| |/ _ \| '_ \/ __|
  |_      _| | |__| |_| \__ \ || (_) | | | | | | |  __/  __/ |  | | | | | | \__ \__ \ | (_) | | | \__ \
    |_||_|    \____\__,_|___/\__\___/|_| |_| |_| |_|   \___|_|  |_| |_| |_|_|___/___/_|\___/|_| |_|___/
                                                                                                       
 
"""

tickets_ct = ContentType.objects.get(
    app_label='managements',
    model='tickets'
)

can_view_all = Permission.objects.create(
    name='Can view all tickets',
    content_type=tickets_ct,
    codename='view_all_tickets'
)

can_add_tickets = Permission.objects.get(
    content_type__app_label='managements',
    content_type__model='tickets',
    codename='add_tickets'
)

mortals = Group.objects.get(name='mortals')
mortals.permissions.add(
    can_view_all
)

angels = Group.objects.get(name='angels')
angels.permissions.add(
    can_view_all,
    can_add_tickets
)