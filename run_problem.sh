#!/usr/bin/env bash

echo -n "Please enter the serial number of the problem you want to solve : "

# shellcheck disable=SC2162
read -r numberInput

problemInput="problems/problem_${numberInput}.py"

output="$(python "${problemInput}")"

echo "Solution : ${output}"