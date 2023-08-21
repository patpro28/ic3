from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Question(models.Model):
    code = models.CharField(_('code'), max_length=10, unique=True,
                            help_text=_('Unique code for search the question'))
    description = models.TextField(_("description"))
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name=_("author"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    category = models.ForeignKey('education.Category', on_delete=models.CASCADE, verbose_name=_("category"))
    level = models.ForeignKey('education.Level', on_delete=models.CASCADE, verbose_name=_("level"))
    
    def __str__(self):
        return self.code
    
