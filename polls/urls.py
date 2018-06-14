from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # list Class
    #  path('aaa', views.ListView.as_view(), name='list2'),

    # list Class
    path('list', views.ListView2.as_view(), name='list'),   # url 접속시 name으로 찾는다

    # list
    path('list2', views.listView),

    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # test
    path('test', views.testView),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('img', views.upload_file, name='img'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)