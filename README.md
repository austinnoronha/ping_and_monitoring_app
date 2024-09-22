# Ping APIs and Monitoring Application

## Project Summary
This project is designed to ping APIs at regular intervals to ensure their uptime and functionality. It is an open-source project, and contributions are welcome to help improve its features. Our goal is to provide an easy-to-use application for monitoring APIs, with an intuitive user interface that offers real-time API health status visualization.

## Objectives
1. **Ping APIs:** We will build a module that can ping APIs at a configurable interval to verify their operational status. These APIs can follow standards such as OpenAPI or Swagger.
2. **Monitor APIs:** The next step will be to build a visual monitoring interface that displays API health in charts using **D3.js**. The UI will be built using **Bootstrap** and **JQuery** for smooth interaction.

## Technologies
We will be using the following technologies:
- **Python (FastAPI)**: For building the backend service to handle API requests and pings.
- **D3.js**: For rendering real-time charts and API monitoring visualizations.
- **Bootstrap and JQuery**: For the front-end UI framework and interaction.
- **Poetry**: As the Python package manager for dependencies.
- **Pytest**: For unit testing.
- **Ruff**: For linting to ensure code quality.

## Project Goals
- **API Health Check**: Continuously ping multiple APIs, verify their responses, and flag any issues.
- **Monitoring Dashboard**: Show historical and real-time data for each API on an interactive graphical interface.
- **Open Source**: Allow developers to contribute easily.

## How to Get Started
### 1. Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Poetry (for package management)
- Docker (optional, for deployment)

### 2. Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ping-api-monitoring.git
   cd ping-api-monitoring

### 3. Run App
   ```bash
   poetry run uvicorn app.main:app --reload

   # run test
   poetry run pytest
   #or
   pytest

## Common Settings

## Poetry
Activate the Poetry Virtual Environment
Once you've installed your dependencies with Poetry, you can activate the virtual environment.
   ```bash
   poetry shell


To exit
   ```bash
   exit

## Ruff
To set up Ruff (a linter) and integrate it with your project using Poetry, follow these steps:
`poetry add --dev ruff`

This will install Ruff and add it to your pyproject.toml file under the [tool.poetry.dev-dependencies] section.

Configure Ruff in the pyproject.toml
Once Ruff is installed, you need to configure it. Open your `pyproject.toml` file and add a `[tool.ruff]` section like this:

```bash
[tool.ruff]
line-length = 88  # Set the maximum line length (similar to black or flake8)
target-version = "py39"  # Target Python version

[tool.ruff.per-file-ignores]
# Ignore specific rules in certain files or directories
"tests/*" = ["F401"]  # Ignore unused imports in tests

# Enable specific rules or exclusions (optional)
# Uncomment and customize based on your project needs
# select = ["E", "F", "I", "N", "A"]
# ignore = []
```

Summary of Commands
- Install Ruff: `poetry add --dev ruff`
- Run Linting: `poetry run ruff check .`
- Fix Linting Issues: `poetry run ruff fix .`
- Set Up Pre-commit (optional): `poetry run pre-commit install`