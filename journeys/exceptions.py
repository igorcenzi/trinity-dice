from rest_framework.exceptions import APIException

class JourneyEndedError(APIException):
    status_code = 403
    default_detail = "Journey has finished"

class JourneyStartedError(APIException):
    status_code = 403
    default_detail = "Journey has started"