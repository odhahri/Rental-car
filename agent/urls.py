from django.urls import path
from agent.views import AgentViewSet

urlpatterns = [
    path('create/', AgentViewSet.as_view({'post': 'create_agent'})),
    path('list/', AgentViewSet.as_view({'get': 'list_agents'})),
    path('get/<int:pk>/', AgentViewSet.as_view({'get': 'get_agent'})),
    path('update/<int:pk>/', AgentViewSet.as_view({'put': 'update_agent'})),
    path('delete/<int:pk>/', AgentViewSet.as_view({'delete': 'delete_agent'})),
    path('get_by_name/<str:name>/', AgentViewSet.as_view({'get': 'get_agent_by_name'})),
    path('agent_list/', AgentViewSet.as_view({'get': 'agent_list_page'}),name='agent_list_page'),
    path('agent_detail/<int:pk>/', AgentViewSet.as_view({'get': 'agent_detail_page'}),name='agent_detail_page'),
]
