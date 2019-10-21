from django import template

# criando uma template tag
register = template.Library()


# criando novo filtro a cada input
@register.filter(name='addclass')
def addclass(value, arg):
    ''' função recebe o input que será inserido classe css que return input como widget'''
    return value.as_widget(attrs={'class': arg})

