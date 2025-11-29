# RaceLab


### Development

#### Virtual Environment Setup

Using `uv` as the virtual environment manager.

```bash
# Create a new virtual environment (.venv/)
uv venv -p 3.13
# Activate the virtual environment
source .venv/bin/activate
# Install locally in editable mode
uv pip install -e .
# Install development dependencies
uv sync --group dev
```

#### Testing

The test suite uses `pytest`.

```bash
# Run tests
pytest

# Run tests with coverage
coverage erase && \
coverage run -m pytest && \
coverage report -m
```
