# Welcome

The goal of this project is to follow along and explore the [Introduction to LangChain](https://semaphoreci.com/blog/langchain?utm_source=Blog+Newsletter&utm_campaign=36db869a13-Nov_16_2023&utm_medium=email&utm_term=0_2c1357b8be-36db869a13-116474720) blog post from Semaphore.

## Getting started

Please copy `.env.sample` to `.env` and use your OpenAI API key and other desired environment variables.

### Prerequisites

Please make sure that you have the following installed on your development environment:

- [Node.js](https://nodejs.org/en)
- [Python](https://www.python.org)

This code base was initially developed and tested on:

- 2021 14" MacBook Pro
  - Apple M1 Max
  - 64 GB memory
  - 2 TB SSD
  - macOS Sonoma `14.1.1`
    - Node.js `v20.9.0`
    - npm `10.1.0`
    - Python `3.11.1`

### Scripts

This project includes several scripts to get you up and running with your local development environment using `npm` (e.g. `npm run setup`):

- `setup`

  - This script checks to see if a Python virtual environment has been created at `.venv` and installs dependencies from [requirements.txt](./requirements.txt)

- `start`

  - This script uses the Python virtual environment at `.venv` to run the application locally

- `test`

  - This script uses the Python virtual environment at `.venv` and runs the unit tests for our shot chart application

- `test:coverage`

  - This script uses the Python virtual environment at `.venv`, runs the unit tests for our shot chart application, and generates an HTML coverage report at [./htmlcov/index.html](./htmlcov/index.html) that will automatically open in the default web browser on macOS.

- `destroy`
  - This script removes the Python virtual environment at `.venv`
