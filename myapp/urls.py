from django.urls import path #type:ignore
from.import views
urlpatterns=[path('pagehtml/',views.pagehtml),
             path('fsave/',views.fsave),
             path('login/',views.login),
]