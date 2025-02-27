RED    = \033[31m
GREEN  = \033[32m
YELLOW = \033[33m
BLUE   = \033[34m
CYAN   = \033[36m
RESET  = \033[0m

VENV = .venv
PYTHON = python3
PIP = $(VENV)/bin/pip
BLACK = $(VENV)/bin/black
RUFF = $(VENV)/bin/ruff
PYTEST = $(VENV)/bin/pytest
TESTS_DIR = tests

$(VENV): 
	@echo "$(CYAN)Setting up virtual environment...$(RESET)"
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)✅ Setup complete!$(RESET)"

setup: $(VENV)

clean:
	@echo "$(YELLOW)🧹 Removing virtual environment...$(RESET)"
	@rm -rf $(VENV)
	@echo "$(GREEN)✅ Virtual environment removed!$(RESET)"

run: $(VENV)
	@echo "$(BLUE)Running project...(RESET)"
	$(VENV)/bin/python -m uvicorn backend.main:app --reload

#test: $(VENV)
	#@echo "$(CYAN)Running tests with pytest...$(RESET)"
	#$(PYTEST) $(TESTS_DIR) --maxfail=1

# check: format lint test

corpus: $(VENV)
	@echo "$(BLUE)Downloading corpus...(RESET)"
	$(VENV)/bin/python src/corpus/download_corpus.py

format: $(VENV)
	@echo "$(CYAN)🎨 Formatting code with Black...$(RESET)"
	$(BLACK) .

lint: $(VENV)
	@echo "$(CYAN)Running Ruff lint...$(RESET)"
	$(RUFF) check . --fix

check: format lint
	@echo "$(GREEN)✅ Code is ready to commit!$(RESET)"


help:
	@echo "$(YELLOW)Available commands:$(RESET)"
	@echo "  $(GREEN)make setup      $(RESET) -> Install dependencies in a virtualenv (only if not existing)"
	@echo "  $(GREEN)make clean      $(RESET) -> Remove the virtualenv"
	@echo "  $(GREEN)make run        $(RESET) -> Start the FastAPI server"
	@echo "  $(GREEN)make format     $(RESET) -> Format the code with Black"
	@echo "  $(GREEN)make lint       $(RESET) -> Lint the code with Ruff"
	@echo "  $(GREEN)make test       $(RESET) -> Run tests with pytest"
	@echo "  $(GREEN)make check      $(RESET) -> Run all checks (format, lint, test)"

# Définition des .PHONY à la fin
.PHONY: setup clean run format lint check help
# .PHONY: setup clean run format lint test check help
