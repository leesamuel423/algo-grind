# algo-grind

- Python
- Golang
- Java
- C++

## Usage

### Creating New Problems

Create a new problem solution template using one of these commands:

```bash
make go 123    # Create a new Go problem #123
make java 123  # Create a new Java problem #123
make py 123    # Create a new Python problem #123
make cpp 123   # Create a new C++ problem #123
```

Each command will:

- Create necessary directory structure
- Generate template files
- Set up test infrastructure

### Running Tests

To run all tests in the project:

```bash
make test
```

To run tests for a specific problem:

```bash
make test go/0001  # Test Go problem #0001
```

### Checking Problems

Check if a problem solution exists for a given language:

```bash
make check-go 268    # Check if Go problem #268 exists
make check-java 268  # Check if Java problem #268 exists
make check-py 268    # Check if Python problem #268 exists
make check-cpp 268   # Check if C++ problem #268 exists
```

### Formatting

Format all source files across all languages:

```bash
make format
```

This runs `clang-format` (C++), `black` (Python), `gofmt` (Go), and `google-java-format` (Java).

### Git Hooks

Install a pre-commit hook that auto-formats staged files on each commit:

```bash
make install-hooks
```

### Cleanup

Remove Bazel build artifacts:

```bash
make clean
```

### Getting Help

To display all available commands:

```bash
make help
```
