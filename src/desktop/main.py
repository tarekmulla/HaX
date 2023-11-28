"""The entry point to the application"""
# pylint: disable=C0413
from os.path import dirname
from sys import path

path.append(dirname(dirname(__file__)))

from app import App  # noqa: E402

from core.utilities.config import CORE_DIR  # noqa: E402
from core.utilities.db.base import init_db  # noqa: E402
from core.utilities.log import init_log  # noqa: E402

if __name__ == "__main__":
  # import the root of the package
  path.append(CORE_DIR)

  init_log()
  init_db()

  app = App()
  app.run()
