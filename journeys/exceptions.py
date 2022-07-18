from rest_framework.exceptions import APIException

class JourneyEndedError(APIException):
    status_code = 403
    default_detail = "Journey has finished"

class CharacterAdd(APIException):
    status_code = 200
    default_detail = "Character has been added to journey"