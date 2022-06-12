import os
import re

from .colourful_print import colourful_print


class ReadFile(object):
    def __init__(self, path):
        self._file_path = path
        self._file_paras = self._get_file_paras(self._file_path)
        self._file_sentences = self._get_file_sentences(self._file_paras)

    def _get_file_paras(self, path):
        try:
            with open(path, 'r', encoding='utf8') as f:
                return [
                    ''.join(para.split()) for para in f.readlines()
                    if para != '\n'
                ]
        except FileNotFoundError:
            file_name = os.path.basename(path)
            colourful_print('ERROR',
                            'ERROR: File {} Not Found.'.format(file_name))

            return []

    def _get_file_sentences(self, paras):
        sentences = []

        for para in paras:
            sentences.append([
                sentence
                for sentence in re.split(r'，|。|；|：|？|！|“|”|《|》|——', para)
                if len(sentence)
            ])

        return sentences

    def get_paras(self):
        return self._file_paras

    def get_sentences(self):
        return self._file_sentences
