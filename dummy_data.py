import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from blog.models import Post, Comment
from django.contrib.auth.models import User
import random
from faker import Faker



def seed_Post(n):
    fake = Faker()
    author_list = [1, 2, 3, 4, 5, 6]
    flags_list = ['python', 'music', 'developement',
                  'life', 'homepage', 'travel']

    for _ in range(n):
        # Get a random author ID from the author_list
        author_id = author_list[random.randint(0, len(author_list)-1)]

        # Create a User instance with the selected author_id
        author = User.objects.get(pk=author_id)

        # Create a new Post instance with the author
        Post.objects.create(
            title=fake.text(max_nb_chars=30),
            author=author,
            body=fake.text(max_nb_chars=700),
            #tags=flags_list[random.randint(0, len(flags_list)-1)]
        )

    print(f'Seeded {n} posts')


# Example usage: seed 10 posts
#seed_Post(35)

def seed_comments(n):
    fake = Faker()
    users_list = [1, 2, 3, 4, 5, 6, 7]
    flags_list = ['python', 'music', 'developement',
                  'life', 'homepage', 'travel']

    for _ in range(n):
        # Get a random author ID from the author_list
        

        # Create a new Post instance with the author
        Comment.objects.create(
            post=Post.objects.get(id=random.randint(1,42)),
            name=User.objects.get(id=random.randint(1,6)),
            body=fake.text(max_nb_chars=50),
            
        )

    print(f'Seeded {n} Comments')

seed_comments(100)