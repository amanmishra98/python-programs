from django.contrib import admin
from .models import IndianIndices,IndianIndices2,GlobalIndices,GlobalIndices2,BSE,BSE2,NSE,NSE2,Sensex,Nifty,FillAndDill_Cash,FillAndDill_SEBI,FillAndDill_Cash2,Fill_SEBI2

# Register your models here.
admin.site.register(IndianIndices)
admin.site.register(IndianIndices2)
admin.site.register(GlobalIndices)
admin.site.register(GlobalIndices2)
admin.site.register(BSE)
admin.site.register(BSE2)
admin.site.register(NSE)
admin.site.register(NSE2)
admin.site.register(Sensex)
admin.site.register(Nifty)
admin.site.register(FillAndDill_Cash)
admin.site.register(FillAndDill_SEBI)
admin.site.register(FillAndDill_Cash2)
admin.site.register(Fill_SEBI2)
