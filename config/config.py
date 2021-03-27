#!/usr/bin/env python
import configparser
import os
from pathlib import Path


abs_path = Path(os.path.dirname(os.path.abspath(__file__)), 'database.ini')


def parse_configuration():
    config = configparser.ConfigParser()
    config.read(filenames=abs_path)
    return config
