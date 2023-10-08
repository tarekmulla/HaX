"""Attack manager module to perform and manage a series attacks on sepecific target"""

from threading import Thread

from classes.crack.crack_base import CrackBase
from classes.crack.enums import CrackType


class CrackPassManager:
  """Class to manage performing a crack password"""
  def start(self, crack: CrackBase, hash_pass, update_status_func):
    """Start the cracking operation in separate thread"""
    self.crack_thread = Thread(
        target=self._start_crack,
        args=(
          crack,
          hash_pass,
          update_status_func,
        ),
    )
    self.crack_thread.start()

  def _start_crack(self, crack: CrackBase, hash_pass, update_status_func):
    """Initiate the attack using all provided payloads"""
    self.stop_flag = False
    if crack.crack_type == CrackType.RAINBOW:
      crack.start(hash_pass, lambda: self.stop_flag, update_status_func)
    self.is_finish = True

  def stop(self):
    """Stop the crack"""
    self.stop_flag = True
