#!/bin/bash

awk '{sum+=$3} END {print {0}, sum}'

