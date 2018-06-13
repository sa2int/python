from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # list Class
  #  path('aaa', views.ListView.as_view(), name='list2'),

    # list Class
    path('bbb', views.ListView2.as_view(), name='list3'),

    # list
    path('list', views.listView),


    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # test
    path('test', views.testView),

    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
