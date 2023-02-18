#!/bin/bash

INPUT_FOLDER=$HOME
EXTENSION='.'
BACKUP_FOLDER=$HOME
ARCHIVE_NAME='backup'
while [ $# -gt 0 ]
do
    key=$1
    
    case $key in 
        --input_folder)
            INPUT_FOLDER=$2
            shift 2
        ;;
        --extension)
            EXTENSION="*.${2}"
            shift 2
            ;;
        --backup_folder)
            BACKUP_FOLDER=$2
            shift 2
            ;;
        --backup_archive_name)
            ARCHIVE_NAME=$2
            shift 2
            ;;
        *)
            echo "$key not recognised"
            shift # shift 1
            ;;
    esac
done

mkdir $BACKUP_FOLDER  &> /dev/null

find $INPUT_FOLDER -name $EXTENSION -exec cp -rp --parent {} $BACKUP_FOLDER \;
tar -cvf $ARCHIVE_NAME $BACKUP_FOLDER  &> /dev/null
echo done
