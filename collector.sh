#!/bin/bash

echo -e "\nScript executed from: ${PWD}"
BASEDIR=$(dirname $0)

COLLECTOR_DIRECTORY="${BASEDIR}/feature_collector/"

if [ ! -d "$PATCH_DIRECTORY" ]; then
    echo "There is no feature_collector"
fi


touch .bash_aliases

vi .bash_aliases