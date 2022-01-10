from django.core.management.base import BaseCommand
from profiles.models import UserProfile
from followers.models import Follower
from wall.models import Post


class Command(BaseCommand):


    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write('Success')


    def create_user(self):
        for i in range(10):
            user = UserProfile.objects.create(
                username=f'test {i+2}',
                email=f'test{i}@gmail.com',
                is_active=True,
                middle_name=f'test {i}',
                phone=f'1234567898745{i}',
                gender=1
                )
            user.set_password('dhsfyus')
            user.save()


    def create_follower(self):
        user_list = UserProfile.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(user_id=user, subscriber_id=1)


    def create_post(self):
        user_list = UserProfile.objects.all()
        for user in user_list:
            for i in range(10):
                Post.objects.create(text=f"Test post{i}", user=user)