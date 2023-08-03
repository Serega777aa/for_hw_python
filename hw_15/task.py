# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import os
from collections import namedtuple
import logging

logging.basicConfig(filename='hw15.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def logging_information(path_dir):
    Obj = namedtuple('Obj', ['name', 'ext', 'directory', 'root'])

    for root, dirs, files in os.walk(path_dir):
        for dir_ in dirs:
            logger.info(Obj(dir_, None, 'True', os.path.basename(root)))
        for file in files:
            logger.info(Obj(file[:file.rfind('.')], file[file.rfind('.'):], 'False', os.path.basename(root)))


parser = argparse.ArgumentParser()
parser.add_argument('path_dir', metavar='path_dir', type=str)
args = parser.parse_args()
logging_information(args.path_dir)