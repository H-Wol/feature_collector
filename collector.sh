#!/bin/bash

echo -e "\nScript executed from: ${PWD}"

DIR="$( cd "$( dirname "$0" )" && pwd -P )"

COLLECTOR_FILE="${DIR}/feature_collector/app.py"


if [ ! -e "$COLLECTOR_FILE" ]; then
    echo "There is no feature_collector"
    exit
fi


touch .bash_aliases
REPLACE="\ "

COLLECTOR_FILE=$(echo ${COLLECTOR_FILE}|  sed  's/\s/\\/g')


echo "alias kisa='python3 "${COLLECTOR_FILE}"'" >> .bash_aliases

source ./.bash_aliases

echo "alias kisa='python3 "${COLLECTOR_FILE}"'" >> ~/.bashrc

source ~/.bashrc

