"""The entry point to the application"""
# pylint: disable=C0413
from os.path import dirname
from sys import path

path.append(dirname(dirname(__file__)))

from app import App  # noqa: E402
from haxcore import CORE_DIR, init_db, init_log  # noqa: E402

if __name__ == "__main__":
  # import the root of the package
  path.append(CORE_DIR)

  init_log()
  init_db()

  app = App()
  app.run()
