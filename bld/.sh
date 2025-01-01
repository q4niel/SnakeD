#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
python3 -B $projDir/bld/src/main.py