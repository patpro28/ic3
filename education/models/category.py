from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True,
                            help_text=_('Unique name for search the category'))
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("categories")
        ordering = ['name']

class Level(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True,
                            help_text=_('Unique name for search the level'))
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = _("levels")
        ordering = ['name']