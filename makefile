# .SILENT:

VENV_DIR = .venv
BIN = $(VENV_DIR)/bin
# path to binaries (executable files)

.PHONY: test

venv:
	python -m venv $(VENV_DIR)

303:
	$(BIN)/python progmerovingio/src/app.py

pip:
	# $(BIN)/pip install pytest

test:
	$(BIN)/pytest -sv

test_entry_coin:
	$(BIN)/pytest -sv progmerovingio/tests/test_303.py::test_entry_coin