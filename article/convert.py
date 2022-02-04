# coding=utf-8
import subprocess


def markdown2html(markdown_text, template=False, standalone=False):
    mathjax_url = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    template_url = "http://localhost:8000/api/pages?name=template.html"
    cmd = [
        'pandoc',
        '-f', 'markdown',
        '-t', 'html',
        '--mathjax=' + mathjax_url,
    ]
    if template:
        cmd.append('--template')
        cmd.append(template_url)

    if standalone:
        cmd.append('-s')
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, input=markdown_text.encode('utf-8'))
    return proc.stdout.decode('utf-8')
