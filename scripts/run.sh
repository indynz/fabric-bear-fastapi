#!/bin/zsh

# Check if the correct number of arguments are provided
if [ $# -ne 4 ]; then
  echo "Usage: ./run.sh <command> <text> <pattern> <title>"
  exit 1
fi

COMMAND="$1"
TEXT="$2"
PATTERN="$3"
TITLE="$4"

# FastAPI endpoint URL
ENDPOINT="http://localhost:8542/fabric"

# Create the JSON payload
PAYLOAD=$(jq -n --arg command "$COMMAND" --arg text "$TEXT" --arg pattern "$PATTERN" --arg title "$TITLE" '{"command":$command, "text":$text, "pattern":$pattern, "title":$title}')

# Send the request to the FastAPI endpoint
RESULT=$(curl -s -X POST -H "Content-Type: application/json" -d "$PAYLOAD" "$ENDPOINT")

# Output the result
echo "$RESULT"