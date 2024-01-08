from django.urls import path
from .views import create_request, view_requests, take_request, view_solution, close_request, view_closed_requests, \
    closed_requests_report, view_engineer_requests

urlpatterns = [
    path('create/', create_request, name='create_request'),
    path('view/', view_requests, name='view_requests'),
    path('take/<int:request_id>/', take_request, name='take_request'),
    path('view_solution/<int:request_id>/', view_solution, name='view_solution'),
    path('close/<int:request_id>/', close_request, name='close_request'),
    path('view_closed_requests/', view_closed_requests, name='view_closed_requests'),
    path('closed_requests_report/', closed_requests_report, name='closed_requests_report'),
    path('view_engineer_requests/', view_engineer_requests, name='view_engineer_requests'),
]

