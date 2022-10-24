#!/bin/bash

echo -e "\nScript executed from: ${PWD}"


DIR="$( cd "$( dirname "$0" )" && pwd -P )" #절대 경로

COLLECTOR_FILE="${DIR}/feature_collector/app.py" #실행할 app.py의 경로 지정


if [ ! -e "$COLLECTOR_FILE" ]; then  #실행할 app.py가 없을 경우 종료
    echo "There is no feature_collector"
    exit
fi


# touch .bash_aliases
# REPLACE="\ "

# COLLECTOR_FILE=$(echo ${COLLECTOR_FILE}|  sed  's/\s/\\/g')


# echo "alias kisa='python3 "${COLLECTOR_FILE}"'" >> .bash_aliases

# source ./.bash_aliases

echo "alias kisa='python3 "${COLLECTOR_FILE}"'" >> ~/.bashrc #alias 지정

source ~/.bashrc #변경사항 저장

