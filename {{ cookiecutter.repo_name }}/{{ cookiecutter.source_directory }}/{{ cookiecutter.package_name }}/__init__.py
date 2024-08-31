import sys
import os

# Get the absolute path to the src directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the src directory to the system path
if src_path not in sys.path:
    sys.path.insert(0, src_path)