import random
from faker import Faker

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDjangoApp.settings')


django.setup()

# FAKE POPULATION SCRIPT

from first_app.models import AccessRecord, Webpage, Topic, User

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        print("populating %d" % (entry))
        # get the topic for entry
        # top = add_topic()
        # # create a fake url
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        # fake_name = fakegen.company()
        # # create a new webpack entry
        # wepg = Webpage.objects.get_or_create(
        #     topic=top, url=fake_url, name=fake_name)[0]
        # # create a fake access record for that webpage
        # acc = AccessRecord.objects.get_or_create(topic=wepg, date=fake_date)[0]
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
