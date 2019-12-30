import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(path, "compiled"))
sys.path.append(os.path.join(path, "util"))
