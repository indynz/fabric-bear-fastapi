````markdown
# Fabric Bear FastAPI

This project provides a FastAPI endpoint to run Fabric patterns and send the output to Bear notes. It allows you to trigger Fabric commands via an HTTP endpoint, making it easy to integrate Fabric with other applications or workflows.

This assumes that you have setup Fabric with the approrpriate commands in zsh so that if you pass the title, then it automatically invokes the commandline tool for Bear.

## Prerequisites

*   Python 3.7+
*   [Pipenv](https://pipenv.pypa.io/en/latest/)
*   Fabric
*   Bear CLI (`bear`)

## Setup

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd fabric-bear-fastapi
    ```

2.  Install dependencies using Pipenv:

    ```bash
    pipenv install
    ```

3.  Activate the Pipenv shell:

    ```bash
    pipenv shell
    ```

4.  Start the FastAPI server:

    ```bash
    uvicorn app.main:app --port 8542 --reload
    ```

## Calling via Shell Script

1.  Make sure the FastAPI server is running.

2.  Run the `run.sh` script with the command, text, pattern, and title as arguments:

    ```bash
    ./scripts/run.sh "echo" "Your long text to summarize" "summarize" "Title of the Bear note"
    ```

    Example:

    To summarize the text "This is a long text" using the "summarize" pattern and create a Bear note with the title "Summary", run:

    ```bash
    ./scripts/run.sh "echo" "This is a long text" "summarize" "Summary"
    ```

    Another Example:

    To run the "extract_wisdom" pattern on a YouTube video and create a Bear note with the title "Roger Barnes Shows Avel Dro", run:

    ```bash
    ./scripts/run.sh "yt" "https://www.youtube.com/watch?v=Hij5HWAwsbY" "extract_wisdom" "Roger Barnes Shows Avel Dro"
    ```

## Calling via Curl

You can also call the FastAPI endpoint directly using `curl`. Here's an example:

```bash
curl -X POST \
  http://localhost:8542/fabric \
  -H 'Content-Type: application/json' \
  -d '{
    "command": "echo",
    "text": "This is a long text to summarize",
    "pattern": "summarize",
    "title": "Summary via Curl"
  }'
```

Another example: To run the "extract_wisdom" pattern on a YouTube video and create a Bear note with the title "Roger Barnes Shows Avel Dro", run:

```bash
curl -X POST \
  http://localhost:8542/fabric \
  -H 'Content-Type: application/json' \
  -d '{
    "command": "yt",
    "text": "https://www.youtube.com/watch?v=Hij5HWAwsbY",
    "pattern": "extract_wisdom",
    "title": "Roger Barnes Shows Avel Dro"
  }'
```