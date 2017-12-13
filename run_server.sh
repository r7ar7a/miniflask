#!/usr/bin/env bash
set -eu
this_dir="$(dirname "$0")"

PYTHONPATH="$this_dir" "$this_dir/miniflask/run_server.py"