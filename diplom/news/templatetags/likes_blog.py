
from django import template


from apinews.models import Like

register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context, blog_post_id):
    request = context['request']
    print(f"************{blog_post_id}***********************")
    try:
        blog_likes = Like.objects.get(post_id = blog_post_id, user=request.user.id).like
        print(f"************{blog_likes}***********************")
    except Exception as err:
        print(err)
        blog_likes = False
        return blog_likes

@register.simple_tag(takes_context=True)
def blog_likes_id(context, blog_post_id):
    request = context['request']
    return Like.objects.get(post_id =blog_post_id, user=request.user.id).id