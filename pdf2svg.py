import os
import subprocess

import click
from tqdm import tqdm

@click.command()
@click.option('-r', '--root', required=True, help='directory of pdf files')
def pdf2svg(root):
    for f in tqdm(os.listdir(root), total=len(os.listdir(root))):
        pdf = os.path.join(root, f)
        if f.lower().endswith(('.pdf', )):
            svg = pdf[:-3] + 'svg'
            subprocess.run(f'inkscape -z -l {svg} -f {pdf}', shell=True)

if __name__ == '__main__':
    pdf2svg()

