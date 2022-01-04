# pdfslicer
simple tool for slicing pages out of pdfs to new pdfs

create a pages.csv with page numbers on lines, 1 per line
edit variables at the top of Makefile as required
make

## doing this as a loop
an example of this as a single loop is in as_loop.tex. if the splits are _very_ large this may be necessary.

## adjusting parameters
parameters are controlled in spec.json
in particular this is where you control landscape vs portrait

## multirun

this depends on two files:
a csv with 2 columns: filenme, page. default spec.csv
a json with the header setup spec.  default spec.json
