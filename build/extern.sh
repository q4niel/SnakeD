#!/bin/bash
projDir=$(dirname $(dirname "$(realpath "$0")"))
nohup python3 -B $projDir/build/bin/main.py run > /dev/null 2>&1 &