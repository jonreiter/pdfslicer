#!/bin/bash
pdfseparate 1.pdf 1_split_%d.pdf
pdfseparate 2s.pdf 2s_split_%d.pdf
pdfseparate 3s.pdf 3s_split_%d.pdf
pdfseparate 3.pdf 3_split_%d.pdf
pdfseparate 4.pdf 4_split_%d.pdf
pdfseparate 1s.pdf 1s_split_%d.pdf
pdfseparate 2.pdf 2_split_%d.pdf
pdfseparate 5.pdf 5_split_%d.pdf
touch doc.tex
cat header.txt >> doc.tex
./gen_latex.sh 1.pdf0.csv 1_split_ >> doc.tex
./gen_latex.sh 1s.pdf1.csv 1s_split_ >> doc.tex
./gen_latex.sh 2.pdf2.csv 2_split_ >> doc.tex
./gen_latex.sh 2s.pdf3.csv 2s_split_ >> doc.tex
./gen_latex.sh 3.pdf4.csv 3_split_ >> doc.tex
./gen_latex.sh 3s.pdf5.csv 3s_split_ >> doc.tex
./gen_latex.sh 4.pdf6.csv 4_split_ >> doc.tex
./gen_latex.sh 5.pdf7.csv 5_split_ >> doc.tex
cat footer.txt >> doc.tex
