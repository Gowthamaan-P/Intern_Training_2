#!/bin/bash

clear

rm -r /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern/aeroproj/*

cp -r aeroproj m2c.sh /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern

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



    git commit -m "$commit_message"

    git status
    sleep 2

    git push -u origin main
}

git_message() {
    clear
    echo
    echo -e " >> ${GREEN}${BOLD}1 Feature${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}2 Bugfix${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}3 Security${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}4 Documentation${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}5 Style${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}6 Test${NORMAL}"
    echo
    read -p "${BOLD}0ffS3c-v3nu enter your choice (1/2/3/4/5/6):${NORMAL} " choice1

    case "$choice1" in
        1)
            commit_type="feat"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            ;;
        2)
            commit_type="bugfix"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            
            ;;
        3)
            commit_type="security"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            
            ;;
        4)
            commit_type="doc"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            
            ;;
        5)
            commit_type="style"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            
            ;;
        6)
            commit_type="test"
            echo -e "\e[1;33mCommit message01:\e[0m"
            read commit_message01
            
            ;;
    esac
    echo 
    echo -e "\e[1;33mCommit message02:\e[0m"
    echo 
    echo -n "$commit_type($commit_message01): "
    read commit_message02
    commit_message="$commit_type($commit_message01): $commit_message02"
    echo
    echo -e "__________________________________________________________________________________________________________"
    echo -e "Your Commit Message: ${YELLOW}${BOLD}$commit_message${NORMAL}" 
    echo -e "__________________________________________________________________________________________________________"
    sleep 4

}

while true; do
    echo
    echo -e "${YELLOW}Script by Venukanthan - https://github.com/itsvenu22${NORMAL}"
    echo
    echo -e "${BOLD}Which repository do you want to commit to?${NORMAL}"
    echo
    echo -e " >> ${GREEN}${BOLD}1 Intern Repo${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}2 Backup Repo${NORMAL}"
    echo -e " >> ${GREEN}${BOLD}3 Both Repo${NORMAL}"
    echo -e " >> ${RED}${BOLD}4 Exit${NORMAL}"
    echo
    read -p "${BOLD}0ffS3c-v3nu enter your choice (1/2/3/4):${NORMAL} " choice

    case "$choice" in
        1)
            git_message
            intern_repo
            ;;
        2)
			git_message	
            backup_repo
            ;;
        3)
			git_message	
            intern_repo
            backup_repo
            ;;
        4)
            echo
            print_message "$GREEN" "Exiting the script."
            echo
            for i in {5..1}; do
                echo -ne "$GREEN""Cleaning terminal in ""$i"
                sleep 1
                echo -ne "\033[1K\r"  
            done

            clear
            exit 0
            ;;
        *)
            clear
            echo
            echo
            print_message "$RED" "Yooooooooooo :\ "
            ;;
    esac
done

