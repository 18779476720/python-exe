import os
import sys
import logging
from configparser import ConfigParser
from concurrent.futures import ProcessPoolExecutor

from pdf2docx import Converter


def pdf_to_word(pdf_file_path, word_file_path):
    cv = Converter(pdf_file_path)
    cv.convert(word_file_path)
    cv.close()


def main(pdf_folder,word_folder):
    logging.getLogger().setLevel(logging.ERROR)


    tasks = []
    with ProcessPoolExecutor(max_workers=int(2)) as executor:
        for file in os.listdir(pdf_folder):
            extension_name = os.path.splitext(file)[1]
            if extension_name != ".pdf":
                continue
            file_name = os.path.splitext(file)[0]
            pdf_file = pdf_folder + "/" + file
            word_file = word_folder + "/" + file_name + ".docx"
            print("正在处理: ", file)
            result = executor.submit(pdf_to_word, pdf_file, word_file)
            tasks.append(result)
    while True:
        exit_flag = True
        for task in tasks:
            if not task.done():
                exit_flag = False
        if exit_flag:
            print("完成")
            exit(0)


if __name__ == "__main__":
    pdf_folder = ''
    word_folder = ''
    main(pdf_folder,word_folder)