import argparse
import json
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", type=str, default="spec.json")
    parser.add_argument("--out", type=str, default="header.txt")
    args = parser.parse_args()

    if os.path.isfile(args.spec):
        with open(args.spec, 'r') as f:
            d = json.load(f)
    else:
        d = {}

    papertype = d.get('papertype', 'a4paper')
    documentclass = d.get('documentclass', 'article')
    geometry = d.get('geometry', 'landscape')

    outtext = (
        '\documentclass[' + papertype + ']{' + documentclass + '}\n' +
        r'\usepackage{geometry}' + '\n' +
        r'\geometry{' + geometry + '}\n' +
        '\n' +
        r'\usepackage{pdfpages}' + '\n' +
        r'\usepackage{pgffor}' + '\n' +
        '\n' +
        r'\begin{document}' + '\n' +
        '\n'
    )
    with open(args.out, 'w') as f:
        f.write(outtext)

main()

# eof
