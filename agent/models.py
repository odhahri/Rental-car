from django.db import models

from app_localtion_car_ssr_project.shared.models.baseUser import BaseUser

class Agent(BaseUser):
    agent_id = models.AutoField(primary_key=True)  

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        db_table = "agent"
        verbose_name = "Agent"
        verbose_name_plural = "Agents"