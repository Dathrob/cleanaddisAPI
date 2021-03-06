from django.urls import path

from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('api/users/', user_signup_view),
    path('api/user/<int:id>',UserDetail.as_view()),
    path('api/companies/',CompanyAPIView.as_view()),
    path('api/waste/<int:pk>', waste_detail_view),
    path('api/waste/<int:pk>/update', waste_update_view),
    path('api/waste/delete/<int:pk>', waste_delete_view),
    path('api/waste/seller/<int:seller>', seller_list_view),
    path('api/waste/buyer/<int:buyer>', buyer_list_view),
    path('api/waste/', waste_create_view),
    path('api/report/', report_create_view),
    path('api/report/<int:pk>', report_detail_view),
    path('api/report/<int:pk>/update', report_update_view),
    path('api/report/delete/<int:pk>', report_delete_view),
    path('api/report/reportlist/<int:reportedBy>',report_list_view),
    path('api/publicplace/', publicplace_create_view),
    path('api/publicplace/<int:pk>', publicplace_detail_view),
    path('api/publicplace/<int:pk>/update', publicplace_update_view),
    path('api/publicplace/delete/<int:pk>', publicplace_delete_view),
    path('api/seminar/', seminar_create_view),
    path('api/seminar/<int:pk>', seminar_detail_view),
    path('api/seminar/<int:pk>/update', seminar_update_view),
    path('api/seminar/delete/<int:pk>', seminar_delete_view),
    path('api/workschedule/', workschedule_create_view),
    path('api/workschedule/<int:pk>', workschedule_detail_view),
    path('api/workschedule/<int:pk>/update', workschedule_update_view),
    path('api/workschedule/delete/<int:pk>', workschedule_delete_view),
    path('api/announcement/', announcement_create_view),
    path('api/announcement/<int:pk>', announcement_detail_view),
    path('api/announcement/<int:pk>/update', announcement_update_view),
    path('api/announcement/delete/<int:pk>', announcement_delete_view),
    # path('api/report/',ReportView.as_view()),
    path('api/auth/', jwt_views.token_obtain_pair),
    path('api/auth/refresh', jwt_views.token_refresh),

]
