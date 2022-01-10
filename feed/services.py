from wall.models import Post
from django.conf import settings

class Feed:
    """ Service feeds  """

    def get_post_list(self, user: settings.AUTH_USER_MODEL): #model post has field 'user' __и у него есть некий связь с owner находиться в модели Follower(related_name) и там есть subscriber
        return Post.objects.filter(user__owner__subscriber=user).order_by('-create_date')\
            .select_related('user').prefetch_related('comments')

        # posts = Post.objects.filter(user__owner__subscriber_id=1).order_by('-create_date')\
        #     .select_related('user').prefetch_related('comments') #для теста
        # 
    def get_single_list(self, pk: int): #
        return Post.objects.get(id=pk).order_by('-create_date')


feed_service = Feed()        