# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group, User
from django.db import models
from django.contrib import admin
from django.utils.timezone import datetime

"""
Snnipet

Example of admin model:

    class UserProfile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        alias = models.CharField((u'User Alias'), max_length=30, blank=True)
        date = models.DateField((u'Creation Date'), null=True, default=datetime.now)
        time = models.TimeField((u'Creation Time'), auto_now_add=True, null=True)
        state = models.BooleanField((u'State'), default=False)
        comments = models.TextField((u'Comments'), blank=True)

        def __str__(self):
            return 'user: %s, alias: %s' % (self.user,self.alias)

        class Meta:
            verbose_name = "User Profile"

    class adminUserProfile(admin.ModelAdmin):
        list_display = ('user','alias')

    admin.site.register(UserProfile,adminUserProfile)
"""
