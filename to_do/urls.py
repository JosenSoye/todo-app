from django.urls import path
from . import views

urlpatterns=[
    path('go/', views.show),
    path('sub/',views.sub),
    path('table',views.table),
    path('view/<int:id>',views.view,name='view'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]