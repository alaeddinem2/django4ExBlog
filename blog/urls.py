from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/'
                    ,views.post_detail,name='post_detail'),
    
    #path('posts/',views.ListPostView.as_view())

]


