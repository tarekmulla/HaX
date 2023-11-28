"""Import the application package"""
from os.path import dirname, realpath
from sys import path

# import the root of the package
hax_path = f"{dirname(realpath(__file__))}/../../src"
path.append(hax_path)


TEST_DIR = dirname(__file__)
