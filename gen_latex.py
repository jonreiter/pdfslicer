'''

'''

import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pages', type=str)
    parser.add_argument('--base', type=str)
    args = parser.parse_args()
    lines_raw = []
    with open(args.pages) as f:
        r = csv.reader(f)
        for row in r:
            lines_raw.append(row[0])
    lines = []
    for l in lines_raw:
        if l.find('-') != -1:
            l_s = l.split('-')
            for i in range(int(l_s[0]), int(l_s[1])+1):
                lines.append(str(i))
        else:
            lines.append(l)
    for l in lines:
        print("\includepdf{" + args.base + l + ".pdf}")

main()

# eof