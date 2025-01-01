#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
python3 -B $projDir/bld/bin/main.py