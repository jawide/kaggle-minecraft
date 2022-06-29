import traceback
from aligo import Aligo


if __name__ == "__main__":
    ali = Aligo()
    try:
        ali.move_file_to_trash(ali.get_folder_by_path("minecraft").file_id)
    except:
        traceback.print_exc()
    ali.upload_folder("/root/minecraft")