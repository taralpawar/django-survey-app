

from django.urls import path
from .views import homepage, thankyou, summary, deletesurvey
urlpatterns = [
    path('', homepage),
    path('thankyou/', thankyou),
    path('summary', summary),
    path('delete/<int:id>/', deletesurvey),

]
