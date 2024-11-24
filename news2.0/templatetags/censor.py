from django import template  
import re  

register = template.Library()  

@register.filter  
def censor(value):  
    # Список нежелательных слов  
    bad_words = ['плохое_слово1', 'плохое_слово2']   
    for word in bad_words:  
        value = re.sub(r'(?i)'+re.escape(word), '*' * len(word), value)  
    return value