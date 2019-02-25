from django.conf.urls import url

from dash_docs_app import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<dashboard_id>[0-9]+)/$', views.dashboard_doc_view, name='detail'),
    ]
