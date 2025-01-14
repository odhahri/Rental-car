from django.urls import path
from agent.views import AgentViewSet

app_name = 'agents'
urlpatterns = [
    path('create/', AgentViewSet.as_view({'post': 'create_agent'}),name='create_agent'),
    path('list/', AgentViewSet.as_view({'get': 'list_agents'})),
    path('get/<int:pk>/', AgentViewSet.as_view({'get': 'get_agent'})),
    path('update/<int:pk>/', AgentViewSet.as_view({'put': 'update_agent'}),name='update_agent'),
    path('delete/<int:pk>/', AgentViewSet.as_view({'delete': 'delete_agent'}),name='delete_agent'),
    path('get_by_name/<str:name>/', AgentViewSet.as_view({'get': 'get_agent_by_name'})),
    
]
