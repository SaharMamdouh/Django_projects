from django.urls import path
from .views import index, list, view_data,update,delete,insert
app_name="TODO"
urlpatterns = [
   path('index/', index,name='index'),
   path('list/', list,name='list-data'),
   path('view/<list_id>/', view_data,name='view-data'),
   path('update/<list_id>/',update, name='update-data'),
   path('delete/<list_id>/',delete, name='delete-data'),
   path('insert/',insert, name='insert-data'),
  #  path('TODO/index', admin.site.urls),
]