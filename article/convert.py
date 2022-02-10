# coding=utf-8
import subprocess
from blog.env import HOST


def markdown2html(markdown_text, template=False, standalone=False):
    mathjax_url = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    template_url = HOST + "/static/html/template.html"
    cmd = [
        'pandoc',
        '-f', 'markdown+implicit_figures',
        '-t', 'html',
        '--mathjax=' + mathjax_url,
        '--highlight=zenburn'
    ]
    if template:
        cmd.append('--template')
        cmd.append(template_url)

    if standalone:
        cmd.append('-s')
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, input=markdown_text.encode('utf-8'))
    return proc.stdout.decode('utf-8')
