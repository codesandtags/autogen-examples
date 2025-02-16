# Project Setup Guide

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

## Setup Instructions

1. Install uv if you haven't already:

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate # On Unix/macOS
```

3. List the dependencies installed with `uv`

```bash
uv tree
Resolved 49 packages in 7ms
autogen-examples v0.1.0
├── asyncio v3.4.3
├── autogen-agentchat v0.4.7
│   └── autogen-core v0.4.7
│       ├── jsonref v1.1.0
│       ├── opentelemetry-api v1.30.0
│       │   ├── deprecated v1.2.18
│       │   │   └── wrapt v1.17.2
│       │   └── importlib-metadata v8.5.0
│       │       └── zipp v3.21.0
│       ├── pillow v11.1.0
│       ├── protobuf v5.29.3
│       ├── pydantic v2.10.6
│       │   ├── annotated-types v0.7.0
│       │   ├── pydantic-core v2.27.2
│       │   │   └── typing-extensions v4.12.2
│       │   └── typing-extensions v4.12.2
│       └── typing-extensions v4.12.2
├── autogen-ext[azure, openai] v0.4.7
```

4. Go to any of the subfolders and run the examples

```bash
cd 01-hello-world
```

## Troubleshooting

If you encounter any issues:

1. Ensure your Python version is compatible
2. Try removing the virtual environment and creating a new one
3. Update uv to the latest version: `pip install -U uv`

## TODO

This is a list of TODOs to enhance / improve this project

- [ ] Add a Factory pattern to get the models easier
- [ ] Add a Builder pattern to work better with the util functions
- [ ] Add comprehensive API documentation
- [ ] Create unit tests for core functionality
- [ ] Implement CI/CD pipeline
- [ ] Add code formatting guidelines
- [ ] Create contribution guidelines (CONTRIBUTING.md)
- [ ] Add example configurations for different use cases
- [ ] Improve error handling and logging
- [ ] Add performance benchmarks
- [ ] Create Docker containerization support
- [ ] Write integration tests
