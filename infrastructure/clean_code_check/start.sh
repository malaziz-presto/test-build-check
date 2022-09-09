#!/bin/bash
black . --check
isort . --check
pflake8