from django.contrib import admin

# admin pannel er sathe amader database a j table create korchi seta models er maddhome ei jay niye ashteh hobe
# er por table er nam task k ei jayay niye asha lagbe
from .models import Task # models.py theke Task class ta niye asha
# akon ai task ba table k admin pannel theke dekhar jonno edit korar jonno ba jai kori na keno ei jaygay register kora hoise
@admin.register(Task) # admin a task k add kora jeno admin theke delte edit kora jay


# admin a ami amar table er ki ki column asole dkehte chai er jonno akta class create kore er moddhe varible set kore dichi kivabe kun column k dkehte chai ba rakhte chai
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','completed','created')
    list_filter = ('completed','created')
    search_fields = ('title','description')
    ordering = ('-created',) # descending hisebe dkeha jabe

