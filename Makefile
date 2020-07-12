
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

default: split latex join

split:
	pdfseparate ${FILEBASE}.pdf ${SPLITBASE}%d.pdf

latex:
	touch ${OUTFILE}.tex
	cat ${HEADERFILE} >> ${OUTFILE}.tex
	./gen_latex.sh ${PAGESFILE} ${SPLITBASE} >> ${OUTFILE}.tex
	cat ${FOOTERFILE} >> ${OUTFILE}.tex


join:
	pdflatex ${OUTFILE}.tex

clean:
	rm -f ${SPLITBASE}*.pdf
	rm -f ${OUTFILE}.tex
	rm -f *.doc *.aux

distclean: clean
	rm -f ${OUTFILE}.pdf

