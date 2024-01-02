#!/bin/bash

#to check if $PYFILE is set

if [[ -z "$PYFILE" ]]; then
    echo "Error: Environment variable \$PYFILE is not set."
    exit 1
fi

# to check if the file exists
if [[ ! -f "$PYFILE" ]]; then
    echo "Error: File $PYFILE does not exist."
    exit 1
fi

# Run the Python script
python "$PYFILE"
