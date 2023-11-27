# Use dependency injection to inject apiService into
# the data source handler

# TODO: Use a configuration or factory to change between
# mock service and prod service

from apiService import ApiCallingService, ApiMockService

# TODO: CONFIG's
endpoint = "https://earthquake.usgs.gov/fdsnws/event/1/application.json"
env = 'prod'

class dataSourceHandler():
    # TODO: Error handling and type checking
    def consumeService():
        apiInstance = ApiCallingService()
        print(apiInstance.defineService(endpoint))

    def consumeMockService():
        apiMockInstance = ApiMockService()
        print(apiMockInstance.defineService(endpoint))

