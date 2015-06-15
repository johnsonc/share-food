from panel.admin import site
from .models import *

site.register(FoodCategory)
site.register(MeatIssues)
site.register(ReligiousIssues)
site.register(PackagingCategory)
site.register(TemperatureCategory)
site.register(FoodIngredients)
site.register(DaysOfTheWeek)

