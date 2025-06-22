"""
Setup configuration for Culture Protocol Engine
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="culture-protocol",
    version="0.1.0",
    author="Sistence Café Tech Team",
    author_email="",
    description="Transform AI cognition through the power of culture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/culture-protocol",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.15.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ],
        "llm": [
            "openai>=1.0.0",
            "anthropic>=0.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "culture-protocol=app.main:app",
        ],
    },
)