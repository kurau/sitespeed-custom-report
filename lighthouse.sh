#!/bin/bash

set -e

exec python3 lighthouse.py &
exec python3 lighthouse_a.py
