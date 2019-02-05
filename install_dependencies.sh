#!/usr/bin/env bash
set -eu

function check_command {
  declare command_name
  for command_name in "$@"; do
    compgen -c "$command_name" | grep -xq "$command_name" || (echo "$command_name: command not found, but needed"; false)
  done
}

check_command pip

pip install flask