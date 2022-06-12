#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import time

from algo.repetition_rate_with_matrix import RepetitionRateWithMatrix
from util.handle_args import handle_args
from util.colourful_print import colourful_print
from util.read_file import ReadFile
from util.write_file import WriteFile


def main():
    if handle_args(sys.argv, 3):
        # 命令行参数校验成功

        # 读取原始文件和待比较的文件
        org_file_inst = ReadFile(sys.argv[1])
        cmp_file_inst = ReadFile(sys.argv[2])
        org_sentences = org_file_inst.get_sentences()
        cmp_sentences = cmp_file_inst.get_sentences()

        # 准备要写入的文件
        write_file_inst = WriteFile(sys.argv[3])
        write_file_inst.write_basic_info(sys.argv[1], sys.argv[2])

        matrix_start = time.time()
        colourful_print('INFO', 'Calculating repetition rate with matrix...')
        # 若原始文件和待比较的文件的段落数量均大于0
        if len(org_sentences) and len(cmp_sentences):
            inst = RepetitionRateWithMatrix(org_sentences, cmp_sentences)
            res = inst.calc()
            matrix_end = time.time()
            matrix_time = matrix_end - matrix_start

            if res['success']:
                write_file_inst.write_matrix_res(res['rate'], matrix_time)

                colourful_print('SUCCESS',
                                'Success! ({}s)\n'.format(matrix_time))
            else:
                colourful_print('ERROR', 'Fail! ({})\n'.format(matrix_time))

        write_file_inst.close()
    else:
        # 命令行参数校验失败

        print('EXAMPLE: python main.py origin.txt compared.txt result.txt')


if __name__ == "__main__":
    total_start = time.time()
    main()
    total_end = time.time()

    total_time = total_end - total_start
    print('Total Executing Time: {}s'.format(total_time))
