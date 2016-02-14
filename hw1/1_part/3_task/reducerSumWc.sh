#!/bin/bash

awk '{sumW+=$2} {sumL+=$1} END {print sumW, sumL}'

