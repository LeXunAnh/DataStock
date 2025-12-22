import sys
from pathlib import Path
from dotenv import load_dotenv
import os

# Lấy thư mục cha của app/ (tức là project root)
ROOT = Path(__file__).resolve().parent.parent

# Nếu chưa có trong sys.path thì thêm vào
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# load environment variables from .env
load_dotenv(dotenv_path="datapipe_2/config/.env")

