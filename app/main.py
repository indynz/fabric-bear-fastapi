import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import os
import asyncio

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(filename='logs/fabric_app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

class FabricParams(BaseModel):
    command: str = "echo" # Default command is echo
    text: str
    pattern: str = "summarize"  # Default pattern is "summarize"
    title: str

async def execute_fabric_command(request: FabricParams):
    """
    Executes the Fabric command and handles any exceptions.
    """
    try:
        # Construct the Fabric command with the specified pattern
        full_command = f'{request.command} "{request.text}" | {request.pattern} "{request.title}"'

        # Execute the command using subprocess, explicitly calling zsh and sourcing .zshrc
        process = subprocess.run(
            ["zsh", "-c", f"source ~/.zshrc && {full_command}"],  # Source .zshrc then execute
            capture_output=True,
            text=True,
            check=True
        )

        # Log the output
        logging.info(f"Command executed successfully. Output: {process.stdout}")

    except subprocess.CalledProcessError as e:
        logging.exception(f"Fabric command failed: {e.stderr}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {str(e)}")

@app.post("/fabric")
async def run_fabric_pattern(request: FabricParams):
    """
    Runs a specified Fabric pattern with the given text and sends it to Bear notes.

    Args:
        request (FabricParams): A JSON object containing the text, title for the Bear note, and the Fabric pattern to use.

    Returns:
        dict: A JSON response indicating the success or failure of the operation.

    Raises:
        HTTPException: If there is an error executing the Fabric command.
    """
    # Log the request parameters
    logging.info(f"Request received: {request}")

    # Create a background task to execute the fabric command
    asyncio.create_task(execute_fabric_command(request))

    # Return immediately with a message indicating the request is being processed
    return {
        "status": "processing",
        "message": "Request is being processed in the background.",
        "request_details": request.dict()
    }