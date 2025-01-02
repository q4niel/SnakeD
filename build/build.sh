#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
python3 -B $projDir/build/bin/main.py