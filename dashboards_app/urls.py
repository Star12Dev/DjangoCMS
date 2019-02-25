from django.conf.urls import url

from dashboards_app.views import (
    DashboardDetail, DashboardList, AuthorDashboardList, CategoryDashboardList,
    YearDashboardList, MonthDashboardList, DayDashboardList, TagDashboardList,
    DashboardSearchResultsList)
from dashboards_app.feeds import LatestDashboardsFeed, TagFeed, CategoryFeed

urlpatterns = [
    url(r'^$',
        DashboardList.as_view(), name='dashboard-list'),
    url(r'^feed/$', LatestDashboardsFeed(), name='dashboard-list-feed'),

    url(r'^search/$',
        DashboardSearchResultsList.as_view(), name='dashboard-search'),

    url(r'^(?P<year>\d{4})/$',
        YearDashboardList.as_view(), name='dashboard-list-by-year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        MonthDashboardList.as_view(), name='dashboard-list-by-month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        DayDashboardList.as_view(), name='dashboard-list-by-day'),

    # Various permalink styles that we support
    # ----------------------------------------
    # This supports permalinks with <dashboard_pk>
    # NOTE: We cannot support /year/month/pk, /year/pk, or /pk, since these
    # patterns collide with the list/archive views, which we'd prefer to
    # continue to support.
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)/$',
        DashboardDetail.as_view(), name='dashboard-detail'),
    # These support permalinks with <dashboard_slug>
    url(r'^(?P<slug>\w[-\w]*)/$',
        DashboardDetail.as_view(), name='dashboard-detail'),
    url(r'^(?P<year>\d{4})/(?P<slug>\w[-\w]*)/$',
        DashboardDetail.as_view(), name='dashboard-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        DashboardDetail.as_view(), name='dashboard-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',  # flake8: NOQA
        DashboardDetail.as_view(), name='dashboard-detail'),

    url(r'^author/(?P<author>\w[-\w]*)/$',
        AuthorDashboardList.as_view(), name='dashboard-list-by-author'),

    url(r'^category/(?P<category>\w[-\w]*)/$',
        CategoryDashboardList.as_view(), name='dashboard-list-by-category'),
    url(r'^category/(?P<category>\w[-\w]*)/feed/$',
        CategoryFeed(), name='dashboard-list-by-category-feed'),

    url(r'^tag/(?P<tag>\w[-\w]*)/$',
        TagDashboardList.as_view(), name='dashboard-list-by-tag'),
    url(r'^tag/(?P<tag>\w[-\w]*)/feed/$',
        TagFeed(), name='dashboard-list-by-tag-feed'),

]
