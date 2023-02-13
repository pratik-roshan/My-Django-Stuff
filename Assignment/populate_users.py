import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Assignment.settings')

import django
django.setup()

from appThree.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    
    
    for entry in range(N):
        # fake_name = fakegen.name().split
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        # New Entry
        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name =fake_last_name,
                                          email=fake_email)[0]
        
if __name__ == '__main__':
    print("POPULATING DATABASES")
    populate(20)
    print("COMPLETE!")

