#!/bin/bash

echo "========== Start Orchestrate the ETL Pipeline =========="

# Virtual Environment Path
VENV_PATH="/home/ricofebrian/projects/simple-etl/etl_projects/bin/activate"

# Activate Virtual Environment
source "$VENV_PATH"

# Set Python Script
PYTHON_SCRIPT="/home/ricofebrian/projects/simple-etl/etl.py"

# Run Python Script & Logging
python "$PYTHON_SCRIPT" >> /home/ricofebrian/projects/simple-etl/log/logfile.log 2>&1

# Logging configuration
dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "Luigi Started at ${dt}" >> /home/ricofebrian/projects/simple-etl/log/luigi-info.log

echo "========== Finish Orchestrate the ETL Pipeline =========="
