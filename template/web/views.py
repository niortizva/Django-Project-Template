# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render
import traceback

def test(request):
    return HttpResponse("Hola Mundo")
