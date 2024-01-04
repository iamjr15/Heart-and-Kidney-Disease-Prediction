import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from resource import load_csv, get_train_test_split, save_result
from resource.c_model_metrics import train_models

import pandas as pd
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')