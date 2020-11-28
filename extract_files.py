import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", type=str, default="spec.csv")
    parser.add_argument("--out", type=str, default="doc.tex")
    args = parser.parse_args()

    f = open(args.spec, 'r')
    r = csv.reader(f)
    pdf_filenames = []
    csv_filenames = []
    cur_filename = None
    split_stubs = []
    fileidx = 0
    for row in r:
        filename = row[0]
        page = row[1]
        pdf_filenames.append(filename)

        if filename != cur_filename:
            # new file
            csv_name = filename+str(fileidx)+'.csv'
            fileidx += 1
            csv_filenames.append(csv_name)
            pdf_base = filename.split('.')[0]
            split_name = pdf_base + '_split_'
            split_stubs.append(split_name)
            outf = open(csv_name, 'w')
            cur_filename = filename
        outf.write(page + "\n")

    unique_pdf_names = list(set(pdf_filenames))

    print("#!/bin/bash")
    for n in unique_pdf_names:
        pdf_base = n.split('.')[0]
        separate_name = pdf_base + '_split_%d.pdf'
        print("pdfseparate " + n + " " + separate_name)
    texfile = args.out
    print("touch " + texfile)
    print("cat header.txt >> " + texfile)

    for i in range(len(csv_filenames)):
        csv_filename = csv_filenames[i]
        split_stub = split_stubs[i]
        print("./gen_latex.sh " + csv_filename + " " + split_stub + " >> " + texfile)

    print("cat footer.txt >> " + texfile)

main()

