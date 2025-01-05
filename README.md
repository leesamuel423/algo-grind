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
