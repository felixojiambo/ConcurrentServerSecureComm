# ConcurrentServerSecureComm Server Project

## Overview

The project is  Python-based server application designed to perform efficient search operations on a dataset. This project includes a server script, tests, and utilities for benchmarking and speed testing.

## Features

- Implements two search algorithms: Linear Search and Binary Search (conceptual).
- Supports searching for a specific string within the dataset.
- Includes a setup for packaging and distribution.
- Utilizes setuptools for package management.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

### Clone the Repository

```bash
git clone https://github.com/felixojiambo/ConcurrentServerSecureComm.git
```

### Install Dependencies

Navigate to the project directory and install the required dependencies:

```bash
cd qf
pip install -r requirements.txt
```

## Usage

### Running the Server Script

To run the server script, use the following command:

```bash
python qf/server/server.py
```

### Searching for a String

To search for a specific string within the dataset, use the following command:

```bash
python qf/server/benchmarking.py <search_string>
```

Replace `<search_string>` with the string you want to search for.

## Testing

To run the tests, navigate to the `tests` directory and execute:

```bash
pytest
```

## Packaging and Distribution

This project is set up for packaging and distribution. To create a distribution package, run:

```bash
python setup.py sdist bdist_wheel
```

To install the package locally for testing, use:

```bash
pip install .
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or support, please contact:

- Felix
- felixojiamboe@gmail.com

## Acknowledgments

- Thanks to the Python community for their support and resources.
```