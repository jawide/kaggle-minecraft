import os
import shutil
import traceback
from aligo import Aligo


if __name__ == "__main__":
    if os.path.exists("/root/minecraft"):
        shutil.rmtree("/root/minecraft")
    ali = Aligo()
    try:
        ali.download_folder(ali.get_folder_by_path("minecraft").file_id, "/root")
    except:
        traceback.print_exc()