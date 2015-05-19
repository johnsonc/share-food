from django.contrib import admin
from .models import *

admin.site.register(FoodCategory)
admin.site.register(MeatIssues)
admin.site.register(ReligiousIssues)
admin.site.register(PackagingCategory)
admin.site.register(TemperatureCategory)
admin.site.register(FoodIngredients)
admin.site.register(DaysOfTheWeek)

