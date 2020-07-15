#!/bin/bash

set -e

exec python3 info.py &
exec python3 detailed.py &
exec python3 graphs.py
