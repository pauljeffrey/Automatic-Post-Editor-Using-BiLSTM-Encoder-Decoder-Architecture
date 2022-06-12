import os


class WriteFile(object):
    def __init__(self, path):
        self._file_path = path

        self._open()

    def _open(self):
        self._file_obj = open(self._file_path, 'w', encoding='utf8')

    def write_basic_info(self, org_file_path, cmp_file_path):
        self._file_obj.write('原始文件名： {}\n'.format(
            os.path.basename(org_file_path)))

        self._file_obj.write('待比较文件名： {}\n\n'.format(
            os.path.basename(cmp_file_path)))

        self._file_obj.write('【文本重复率运算结果】\n')

    def write_matrix_res(self, rate, time):
        self._file_obj.write('1. 利用二维矩阵查找连续重复的字符串实现\n')
        self._file_obj.write('\t文本重复率： {:.2%}\n'.format(rate))
        self._file_obj.write('\t运算时间： {:.4}s\n'.format(time))

    def close(self):
        self._file_obj.close()
