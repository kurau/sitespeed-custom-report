#!/bin/bash

set -e

exec python3 detailed_parallels_runs.py &
exec python3 graphs.py
