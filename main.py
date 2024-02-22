import argparse
import logging
import os
from collections import namedtuple


def get_dir_info(path: str):
    FileInfo = namedtuple('FileInfo', 'name extension is_catalog parent_dir')
    try:
        os.chdir(path)
    except FileNotFoundError as ex:
        logging.error(ex)
        raise FileNotFoundError(ex)
    infos = []
    for file in os.listdir(path):
        if os.path.isfile(file):
            name, extension = os.path.splitext(file)
            is_catalog = False
        else:
            name = file
            extension = None
            is_catalog = True
        parent_dir = os.path.dirname(os.getcwd())
        infos.append(FileInfo(name=name, extension=extension, is_catalog=is_catalog, parent_dir=parent_dir))

    return infos


if __name__ == "__main__":
    logging.basicConfig(filename="logging.txt",
                        filemode='a',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    parser = argparse.ArgumentParser(description="Введите путь")
    parser.add_argument('path')
    args = parser.parse_args()
    logging.info(f"Введен путь {args.path}")
    try:
        infos = get_dir_info(args.path)
        logging.info(infos)
        print("SUCCESS")
    except FileNotFoundError:
        print("ERROR")

