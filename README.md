#ExpNo 1 :Developing AI Agent with PEAS Description
Name: Shubnum Fathima AB
Register Number: 212225240147

##AIM:
To find the PEAS description for the given AI problem and develop an AI agent.


##Theory:
Medicine prescribing agent:
Such this agent prescribes medicine for fever (greater than 98.5 degrees) which we consider here as unhealthy, by the user temperature input, and another environment is rooms in the hospital (two rooms). This agent has to consider two factors one is room location and an unhealthy patient in a random room, the agent has to move from one room to another to check and treat the unhealthy person. The performance of the agent is calculated by incrementing performance and each time after treating in one room again it has to check another room so that the movement causes the agent to reduce its performance. Hence, agents prescribe medicine to unhealthy.

PEAS DESCRIPTION:
Agent Type	Performance	Environment	Actuators	Sensors
Medicine prescribing agent	Treating unhealthy, agent movement	Rooms, Patient	Medicine, Treatment	Location, Temperature of patient

##DESIGN STEPS
STEP 1:Identifying the input:
Temperature from patients, Location.

STEP 2:Identifying the output:
Prescribe medicine if the patient in a random has a fever.

STEP 3:Developing the PEAS description:
PEAS description is developed by the performance, environment, actuators, and sensors in an agent.

STEP 4:Implementing the AI agent:
Treat unhealthy patients in each room. And check for the unhealthy patients in random room

STEP 5:
Measure the performance parameters: For each treatment performance incremented, for each movement performance decremented

##Program:
```
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
```
##Output:
<img width="560" height="67" alt="image" src="https://github.com/user-attachments/assets/e6c09425-1ddc-4076-b64c-f9f1b2fd4194" />

##Result:
Thus the Developing AI Agent with PEAS Description was implemented using python programming.
