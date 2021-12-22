from django.contrib import admin
from .models import Sale, CSV, Position, DailySale

admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)
admin.site.register(DailySale)


