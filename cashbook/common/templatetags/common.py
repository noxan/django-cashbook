from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.tag
def nav_item(parser, token):
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 3:
        raise template.TemplateSyntaxError, "%r tag requires at least two argument" % template_tag
    return NavItemNode(args[1:])

class NavItemNode(template.Node):
    def __init__(self, args):
        self.label = args[0]
        self.url = reverse(args[1], args=args[2:])

    def render(self, context):
        path = context['request'].path
        link = '<a href="%s">%s</a>' % (self.url, self.label)
        if path == self.url:
            return '<li class="active">%s</li>' % (link)
        return '<li>%s</li>' % (link)
