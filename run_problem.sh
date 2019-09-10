#!/usr/bin/env bash

echo -n "Please enter the serial number of the problem you want to solve : "

read numberInput

problemInput="problems/problem_${numberInput}.py"

output="$(python ${problemInput})"

echo "Solution : ${output}"