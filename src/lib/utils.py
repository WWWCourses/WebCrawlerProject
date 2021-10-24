from pathlib import Path

def get_project_root():
    return Path(__file__).parent.parent.parent

def get_data_path():
    return str(get_project_root())+'/data/'

if __name__ == '__main__':
	print(__file__)
    # print(get_project_root())
    # print(get_data_path())
