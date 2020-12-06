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

    lines = []
    lines.append(r"\documentclass[" + papertype + "]{" + documentclass + "}")
    lines.append(r"\usepackage{geometry}")
    lines.append(r"\geometry{" + geometry + "}")
    lines.append("")
    lines.append(r"\usepackage{pdfpages}")
    lines.append(r"\usepackage{pgffor}")
    lines.append("")
    lines.append(r"\begin{document}")
    lines.append("")

    with open(args.out, "w") as f:
        f.write("\n".join(lines))

main()

# eof
