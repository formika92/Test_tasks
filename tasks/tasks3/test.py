from tasks.tasks1.test import prepare_dict
from tasks.tasks2.test import get_file_name

if __name__ == "__main__":
    print(prepare_dict())
    print(get_file_name(name="file", all_names=["my_file", "my_filename"]))
