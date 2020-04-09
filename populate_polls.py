import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'funProj.settings')
from faker import Faker
import random
import django
django.setup()
from polls.models import Poll


fakegen = Faker()

choices = ['A','B','C']

def populate(N=5):
    
    
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_vote = random.choice(choices)
        poll = Poll.objects.get_or_create(first_name=fake_first_name,
                                            last_name = fake_last_name, 
                                            vote = fake_vote)[0]
if __name__ == '__main__':
    print("POPULATING")
    populate(30)
    print('Finished!')