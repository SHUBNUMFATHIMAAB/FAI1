#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class HealthMonitoringAgent:
    def __init__(self, patient_data):
        self.patient_data = patient_data

    def monitor_health(self):
        while True:
            current_health_state = self.sensors.get_health_state()
            action = self.choose_action(current_health_state)
            self.actuators.perform_action(action)

            if action == "No specific action needed":
                break

    def choose_action(self, current_health_state):
        if current_health_state['heart_rate'] > 120:
            return "Alert healthcare provider: High heart rate detected"
        elif current_health_state['blood_pressure'] > 140:
            return "Alert healthcare provider: High blood pressure detected"
        elif current_health_state['temperature'] > 38:
            return "Recommend rest and monitor temperature"
        else:
            return "No specific action needed"


class HealthSensors:
    def get_health_state(self):
        return {
            'heart_rate': random.randint(60, 150),
            'blood_pressure': random.randint(90, 160),
            'temperature': random.uniform(36.0, 38.5)
        }


class HealthActuators:
    def perform_action(self, action):
        print(action)


if __name__ == "__main__":
    patient_data = {
        'patient_id': 123,
        'name': 'John Doe',
        'age': 35
    }

    health_sensors = HealthSensors()
    health_actuators = HealthActuators()

    health_monitoring_agent = HealthMonitoringAgent(patient_data)

    health_monitoring_agent.sensors = health_sensors
    health_monitoring_agent.actuators = health_actuators

    health_monitoring_agent.monitor_health()


# In[ ]:





# In[ ]:




