from django.contrib.syndication.views import Feed
from blog.models import Blog

class LatestEntriesFeed(Feed):
    title = "moxi's blog"
    link = "/feeds/"
    description = "To know what happened to moxi!"

    def items(self):
        return Blog.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_text

    def item_link(self, item):
        return "blog.zhongmoxi.com/entry/" + str(item.id) + "/"
