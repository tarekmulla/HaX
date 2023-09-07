"""Attack Module"""
from requests import Response

from classes.attacks.enums import AttackType, RequestType


class Attack:
  """Class represents Cyber Attack"""
  payloads: list = []

  def __init__(self, url: str, request_type: RequestType, paramaters: list, attack_type: AttackType):
    self.request_type = request_type
    self.url = url
    self.paramaters = paramaters
    self.attack_type = attack_type

  def is_attack_succeeded(self, response: Response) -> bool:
    """Examine the response to identify whether the attack was successful"""
    return response.status_code == 200
