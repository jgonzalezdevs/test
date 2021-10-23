"""
 
     _  _     ____                         ___                            _       
   _| || |_  / ___|  ___  _ __ ___   ___  |_ _|_ __ ___  _ __   ___  _ __| |_ ___ 
  |_  ..  _| \___ \ / _ \| '_ ` _ \ / _ \  | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
  |_      _|  ___) | (_) | | | | | |  __/  | || | | | | | |_) | (_) | |  | |_\__ \
    |_||_|   |____/ \___/|_| |_| |_|\___| |___|_| |_| |_| .__/ \___/|_|   \__|___/
                                                        |_|                       
 
"""

from django.contrib.auth.models import Group, ContentType
from management.models import GroupType

"""
 
     _  _      ____                           
   _| || |_   / ___|_ __ ___  _   _ _ __  ___ 
  |_  ..  _| | |  _| '__/ _ \| | | | '_ \/ __|
  |_      _| | |_| | | | (_) | |_| | |_) \__ \
    |_||_|    \____|_|  \___/ \__,_| .__/|___/
                                   |_|        
 
"""

angels = Group.objects.create(name='angels')
mortals = Group.objects.create(name='mortals')

angel_user = ContentType.objects.get(app_label='management', model='angel')
mortal_user = ContentType.objects.get(app_label='management', model='mortal')

GroupType.objects.create(user_type=mortal_user, group=mortals)
GroupType.objects.create(user_type=angel_user, group=angels)