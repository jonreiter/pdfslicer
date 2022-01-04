
# the input pdf is FILEBASE.pdf
FILEBASE=arch
# stub for output pdf name
OUTFILE=doc

# name of the file with page numbers
# 1 per line
PAGESFILE=pages.csv

# latex header and footer
HEADERFILE=header.txt
FOOTERFILE=footer.txt

SPLITBASE=${FILEBASE}_split_

# setup for multi-file version
SPECSFILE=spec.csv
SCRIPTFILE=extract_files.py
MULTIFILE_SCRIPT=multifile.sh
HEADERSCRIPT=gen_header.py
HEADERSPEC=spec.json

default: split latex join

header:
	python3 ${HEADERSCRIPT} --spec=${HEADERSPEC} --out=${HEADERFILE}

split:
	pdfseparate ${FILEBASE}.pdf ${SPLITBASE}%d.pdf

latex: header
	touch ${OUTFILE}.tex
	python3 gen_header.py --out=${OUTFILE}.tex
	python3 gen_latex.py --pages=${PAGESFILE}  --base=${SPLITBASE} >> ${OUTFILE}.tex
	cat ${FOOTERFILE} >> ${OUTFILE}.tex


join:
	pdflatex ${OUTFILE}.tex

clean:
	rm -f ${SPLITBASE}*.pdf
	rm -f ${OUTFILE}.tex
	rm -f *.doc *.aux
	rm -f ${MULTIFILE_SCRIPT}
	rm -f *_split_*.pdf
	rm -f *.pdf*.csv

distclean: clean
	rm -f ${OUTFILE}.pdf

multisplit:
	python3 ${SCRIPTFILE} --out=${OUTFILE}.tex --spec=${SPECSFILE} > ${MULTIFILE_SCRIPT}
	chmod u+x ${MULTIFILE_SCRIPT}
	./${MULTIFILE_SCRIPT}

multirun: multisplit latex join
