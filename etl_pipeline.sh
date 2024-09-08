#!/bin/bash

# Virtual Environment Path
VENV_PATH="/home/ricofebrian/projects/simple-etl/etl_projects/bin/activate"

# Activate venv
source "$VENV_PATH"

# set python script
PYTHON_SCRIPT="/home/ricofebrian/projects/simple-etl/etl.py"

# run python script and logging
python "$PYTHON_SCRIPT" >> /home/ricofebrian/projects/simple-etl/log/logfile.log 2>&1

# logging simple
dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "Luigi Started at ${dt}" >> /home/ricofebrian/projects/simple-etl/log/luigi-info.log
