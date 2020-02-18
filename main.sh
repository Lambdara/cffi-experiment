#!/bin/bash
set -e

echo "Running build.py..."

python build.py

echo "Library built"

echo "Running run.py"

python run.py
