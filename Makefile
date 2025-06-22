# 🌈 Culture Protocol Engine - Makefile

.PHONY: help install test run dev clean docker-build docker-run docker-dev

# Default target
help:
	@echo "🌈 Culture Protocol Engine Commands"
	@echo "=================================="
	@echo "install     - Install dependencies and package"
	@echo "test        - Run all tests"
	@echo "run         - Start the API server"
	@echo "dev         - Start development server with hot reload"
	@echo "clean       - Clean up temporary files"
	@echo "docker-build - Build Docker image"
	@echo "docker-run  - Run with Docker Compose"
	@echo "docker-dev  - Run development environment with Docker"
	@echo "docker-down - Stop Docker containers"

# Local development
install:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate && pip install -e .

test:
	pytest -v

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

# Docker commands
docker-build:
	docker-compose build
	docker-compose -f docker-compose.dev.yml build 

docker-run:
	docker-compose up -d
	@echo "🚀 API running at http://localhost:8000"

docker-dev:
	docker-compose -f docker-compose.dev.yml up
	@echo "🛠️  Development server running at http://localhost:8000"
	@echo "📊 Jupyter Lab available at http://localhost:8888"

docker-down:
	docker-compose down
	docker-compose -f docker-compose.dev.yml down

# Development helpers
lint:
	flake8 app tests

format:
	black app tests

type-check:
	mypy app

# All checks
check: lint type-check test

# Setup for new contributors
setup: install test
	@echo "✅ Setup complete! Run 'make dev' to start development server"
