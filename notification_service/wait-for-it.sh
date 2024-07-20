#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

TIMEOUT=15
QUIET=0
HOST="$1"
PORT="$2"

while [ $TIMEOUT -gt 0 ]; do
  nc -z "$HOST" "$PORT" > /dev/null 2>&1
  result=$?
  if [ $result -eq 0 ]; then
    if [ $QUIET -eq 0 ]; then echo "Host $HOST:$PORT is up"; fi
    exit 0
  fi
  TIMEOUT=$(( TIMEOUT - 1 ))
  sleep 1
done

echo "Timeout waiting for $HOST:$PORT"
exit 1
