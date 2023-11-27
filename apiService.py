# Interface for API service
# Includes sub-classes for Mocked and API Calling Service
from abc import ABC, abstractmethod
import requests

class ApiService(ABC):
    @abstractmethod
    def defineService(self, endpoint):
        print('calling api service...')

class ApiCallingService(ApiService):
    def defineService(self, endpoint):
        response = requests.get(endpoint)
        return response.json()

class ApiMockService(ApiService):
    def defineService(self, endpoint):
        response = requests.get(endpoint)
        return response.json()