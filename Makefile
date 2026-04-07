# Default shell
SHELL := /bin/bash

# Colors for pretty printing
GREEN := \033[0;32m
NC := \033[0m # No Color

.PHONY: help go java py cpp check-py check-cpp check-java check-go test clean format install-hooks

help:
	@echo "Usage:"
	@echo "  make go 123       	- Create new Go problem"
	@echo "  make java 123     	- Create new Java problem"
	@echo "  make py 123       	- Create new Python problem"
	@echo "  make cpp 123      	- Create new C++ problem"
	@echo "  make check-py 268 	- Check if Python problem exists"
	@echo "  make check-cpp 268	- Check if C++ problem exists"
	@echo "  make check-java 268	- Check if Java problem exists"
	@echo "  make check-go 268 	- Check if Go problem exists"
	@echo "  make test         	- Run all tests"
	@echo "  make test go/0001 	- Run specific test"
	@echo "  make format       	- Format all source files"
	@echo "  make install-hooks	- Install git pre-commit hook"
	@echo "  make clean        	- Clean Bazel artifacts"

# Create new problems
go:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make go 123"; \
		exit 1; \
	fi
	@echo "Creating Go problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/go_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Go problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

java:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make java 123"; \
		exit 1; \
	fi
	@echo "Creating Java problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/java_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Java problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

py:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make py 123"; \
		exit 1; \
	fi
	@echo "Creating Python problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/py_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Python problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

cpp:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make cpp 123"; \
		exit 1; \
	fi
	@echo "Creating C++ problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/cpp_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created C++ problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

# Check if problem exists
check-py:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make check-py 268"; \
		exit 1; \
	fi
	@./scripts/check.py py $(filter-out $@,$(MAKECMDGOALS))

check-cpp:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make check-cpp 268"; \
		exit 1; \
	fi
	@./scripts/check.py cpp $(filter-out $@,$(MAKECMDGOALS))

check-java:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make check-java 268"; \
		exit 1; \
	fi
	@./scripts/check.py java $(filter-out $@,$(MAKECMDGOALS))

check-go:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make check-go 268"; \
		exit 1; \
	fi
	@./scripts/check.py go $(filter-out $@,$(MAKECMDGOALS))

# Testing
test:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Running all tests..."; \
		TMPFILE=$$(mktemp); \
		bazel test //... 2>&1 | tee "$$TMPFILE"; \
		EXIT_CODE=$${PIPESTATUS[0]}; \
		python3 scripts/test_summary.py "$$TMPFILE"; \
		rm -f "$$TMPFILE"; \
		exit $$EXIT_CODE; \
	else \
		echo "Running test for $(filter-out $@,$(MAKECMDGOALS))..."; \
		bazel test //$(filter-out $@,$(MAKECMDGOALS)):test; \
	fi

# Formatting
format:
	@echo "Formatting C++..."
	@find cpp -name '*.cc' -o -name '*.h' | xargs clang-format -i
	@echo "Formatting Python..."
	@find py -name '*.py' | xargs black --quiet
	@echo "Formatting Go..."
	@find go -name '*.go' | xargs gofmt -w
	@echo "Formatting Java..."
	@find java -name '*.java' | xargs google-java-format -i
	@echo -e "${GREEN}Done${NC}"

# Git hooks
install-hooks:
	@cp scripts/pre-commit .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo -e "${GREEN}Pre-commit hook installed${NC}"

# Cleanup
clean:
	@echo "Cleaning Bazel artifacts..."
	@bazel clean

# This allows for arbitrary arguments
%:
	@: 