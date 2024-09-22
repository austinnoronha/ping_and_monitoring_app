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
