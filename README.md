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

## Usage

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

## Configuration

*   The FastAPI server runs on `http://localhost:8542` by default.
*   Ensure that Fabric and Bear CLI are correctly configured in your environment.  Specifically, the `summarize` command needs to be available in the environment where the FastAPI application is running (e.g., by sourcing your `.zshrc` or setting the `PATH` variable).

## License

MIT