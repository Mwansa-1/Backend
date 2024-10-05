from django.urls import path 
from .views import ReportFormCreateView,ReportFormUpdateView,StatisticsCreateView,StatisticsUpdateView,AlertsCreateView,AlertsUpdateView,DailyUpdatesCreateView,DailyUpdatesUpdateView,BlogCreateView,BlogUpdateView, ResultsCreateView,ResultsUpdateView,ReportFormListView,StatisticsListView,AlertsListView,DailyUpdatesListView,BlogListView,ResultsListView,UserLoginView,UserRegistrationView

urlpatterns = [
    # report urls for the update(and the id field for the url) , and the create views 
    path('report_form_create', ReportFormCreateView.as_view(), name='report_form_create'),
    path('report_form_list', ReportFormListView.as_view(), name='report_form_list'),
    path('report_form_update/<int:pk>/', ReportFormUpdateView.as_view(), name='report_form_update'),
    # statistics urls
    path('statistics_create', StatisticsCreateView.as_view(), name='statistics_create'),
    path('statistics_list', StatisticsListView.as_view(), name='statistics_list'),
    path('statistics_update/<int:pk>/', StatisticsUpdateView.as_view(), name='statistics_update'),
    # alerts urls
    path('alerts_create', AlertsCreateView.as_view(), name='alerts_create'),
    path('alerts_list', AlertsListView.as_view(), name='alerts_list'),
    path('alerts_update/<int:pk>/', AlertsUpdateView.as_view(), name='alerts_update'),
    #dailyupdates urls
    path('dailyupdates_create', DailyUpdatesCreateView.as_view(), name='dailyupdates_create'),
    path('dailyupdates_list', DailyUpdatesListView.as_view(), name='dailyupdates_list'),
    path('dailyupdates_update/<int:pk>/', DailyUpdatesUpdateView.as_view(), name='dailyupdates_update'),
    # blog urls
    path('blog_create', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    # results urls
    path('results_create', ResultsCreateView.as_view(), name='blog_create'),
    path('results_list', ResultsListView.as_view(), name='blog_list'),
    path('results_update/<int:pk>/', ResultsUpdateView.as_view(), name='blog_update'),
    # user urls
    path('user_login', UserLoginView.as_view(), name='user_login'),
    path('user_registration', UserRegistrationView.as_view(), name='user_registration'),

]