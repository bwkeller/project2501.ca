default: cv.pdf

body.tex: ../pages/cv.md Makefile
	pandoc -f markdown -t latex ../pages/cv.md -o body.tex

cv.tex: body.tex header.tex footer.tex Makefile
	cat header.tex > cv.tex
	cat body.tex >> cv.tex
	cat footer.tex >> cv.tex

cv.pdf: cv.tex
	pdflatex cv.tex

clean:
	@rm cv.* body.tex
