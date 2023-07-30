import os
import json
import shutil
from typing import List, Dict

class ShowCreator:
    def __init__(self, folder_name: str, folder_path: str):
        """
        Initialize ShowCreator object.

        Parameters:
            folder_name (str): Name of the main folder.
            folder_path (str): Path to the main folder.
        """
        self.folder_name = folder_name
        self.folder_path = folder_path

    