#!/usr/bin/env python
# encoding=utf-8

"""
@Author  :   zhangchao
@Contact :   
@Project :   AByteOfPythonXmind
@File    :   main.py
@Time    :   2018-07-12 17:19
@Desc    :   
"""
import html2md

HOST = 'https://bop.mol.uno/'
BOOK_URLS = ['index.html',
             '02.dedication.html',
             '03.1.preface.html',
             '03.2.translator-preface.html',
             '04.about_python.html',
             '05.installation.html',
             '06.first_steps.html',
             '07.basics.html',
             '08.op_exp.html',
             '09.control_flow.html',
             '10.functions.html',
             '11.modules.html',
             '12.data_structures.html',
             '13.problem_solving.html',
             '14.oop.html',
             '15.io.html',
             '16.exceptions.html',
             '17.stdlib.html',
             '18.more.html',
             '19.what_next.html', '20.floss.html',
             '21.about.html',
             '22.revision_history.html',
             '23.translations.html',
             '24.Translation-how-to.html',
             '25.Feedback.html',
             ]


def download_convert_md():
    for url in BOOK_URLS:
        result = html2md.UrlToMarkdown().convert(HOST + url)
        with open('md/' + url.replace('.html', '.md'), 'w') as f:
            f.write(result.encode('utf-8'))
            f.close()


if __name__ == "__main__":
    # download_convert_md()
    pass
