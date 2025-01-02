#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
python3 -B $projDir/3rd/bin/main.py