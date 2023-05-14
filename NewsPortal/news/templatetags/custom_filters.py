from django import template

register = template.Library()

BAD_WORDS = {
   'unemployment' : 'u***********',
   'Unemployment' : 'U***********',
   'crisis' : 'c*****',
   'Crisis' : 'C*****',
   'prince' : 'p*****',
   'Prince' : 'P*****',
   'harry'  : 'h****',
   'Harry'  : 'H****',
   'meghan' : 'm*****',
   'Meghan' : 'M*****',
   'markle' : 'm*****',
   'Markle' : 'M*****',
}

@register.filter()
def censor(value):
   if type(value) == str:
      new_text = value
      for w in BAD_WORDS:
         new_text = new_text.replace(w, BAD_WORDS[w])
      return f'{new_text}'
   else:
      return '!!! Broken text !!!'
