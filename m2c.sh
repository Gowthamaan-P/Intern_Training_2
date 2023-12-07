#!/bin/bash

clear

rm -r /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern/aeroproj/*

cp -r aeroproj m2c.sh /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern


#!/bin/bash

BOLD=$(tput bold)
NORMAL=$(tput sgr0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)

print_message() {
    local color="$1"
    local message="$2"
    echo -e "${color}${message}${NORMAL}"
}

intern_repo() {
    cd /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/Intern_Training_2

    echo -e "\e[1;34mMOVED TO \e[1;32mINTERN REPO\e[0m"
    echo -e "__________________________________________________________________________________________________________"
    pwd

    git status
    sleep 2
    echo -e "__________________________________________________________________________________________________________"
    echo -e "<<<<<<YOUR_BRANCH>>>>>>"
    echo -e "__________________________________________________________________________________________________________"
    git branch
    sleep 2
    echo -e "__________________________________________________________________________________________________________"

    git add .
    git status
    sleep 2
    echo -e "__________________________________________________________________________________________________________"

    echo -e "\e[1;33mCommit message:\e[0m"
    read commit_message

    git commit -m "$commit_message"

    git status
    sleep 2

    git push -u origin Venukanthan-BS
}

backup_repo() {
    cd /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern

    clear

    echo -e "\e[1;34mMOVED TO \e[1;32mPERSONAL REPO\e[0m"
    echo -e "__________________________________________________________________________________________________________"
    pwd

    git status
    sleep 2
    echo -e "__________________________________________________________________________________________________________"
    echo -e "<<<<<<YOUR_BRANCH>>>>>>"
    echo -e "__________________________________________________________________________________________________________"

    git branch
    sleep 2
    echo -e "__________________________________________________________________________________________________________"

    git add .
    git status
    sleep 2
    echo -e "__________________________________________________________________________________________________________"

    echo -e "\e[1;33mCommit message:\e[0m"
    read commit_message

    git commit -m "$commit_message"

    git status
    sleep 2

    git push -u origin main
}


while true; do
    echo -e "${BOLD}Which repository do you want to commit to?${NORMAL}"
    echo -e "1. ${GREEN}${BOLD}Intern Repo 1${NORMAL}"
    echo -e "2. ${GREEN}${BOLD}Backup Repo 2${NORMAL}"
    echo -e "3. ${RED}${BOLD}Exit${NORMAL}"

    read -p "${BOLD}Enter your choice (1/2/3):${NORMAL} " choice

    case "$choice" in
        1)
            intern_repo
            ;;
        2)
            backup_repo
            ;;
        3)
            print_message "$GREEN" "Exiting the script."
            exit 0
            ;;
        *)
            print_message "$RED" "Yooooooooooo :\ "
            ;;
    esac
done

