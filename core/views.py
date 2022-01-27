from django.shortcuts import render, HttpResponse
from django.views import View
import json
import os
from src import settings
from .models import *


class IndexView(View):
    def get(self, request):
        query = Currency.objects.all()
        context = {
            "currencies": query,
        }
        if query:
            pass
        else:
            currency_data = []
            file_path = os.path.join(settings.BASE_DIR, 'currency.json')

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for code, name in data.items():
                    country = Currency.objects.create(code=code, name=name)
                    country.save()
                    currency_data.append({'name': name, 'value': code})

        return render(request, "index.html", context)
