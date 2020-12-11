AOC2020_HOME_DIRECTORY = $(PWD)
AOC_PYTHON_DIR = aoc2020

run:
	export PIPENV_VERBOSITY=-1 && pipenv run python aoc2020/day$(DAY).py

run-all: $(AOC_PYTHON_DIR)/day*py
	for dayfile in $^; do \
		echo $${dayfile}; \
		export PIPENV_VERBOSITY=-1; \
		pipenv run python $${dayfile}; \
	done

test:
	cd $(AOC2020_HOME_DIRECTORY) && pipenv run python -m pytest
