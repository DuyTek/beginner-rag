import fireworks.client
import os
import dotenv
import chromadb
import json
from tqdm.auto import tqdm
import pandas as pd
import random
import os

dotenv.load_dotenv()

fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")