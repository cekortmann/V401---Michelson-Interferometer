all: build/v401.pdf

build/v401.pdf: v401.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v401.tex
	lualatex  --output-directory=build v401.tex
	biber build/v401.bcf
	lualatex  --output-directory=build v401.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
