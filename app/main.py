# filepath: /Users/indy/Development/Python/Play/fabric-bear-fastapi/app/main.py
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class FabricParams(BaseModel):
    command: str = "echo" # Default command is echo
    text: str
    pattern: str = "summarize"  # Default pattern is "summarize"
    title: str

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

        # Return the output
        return {"status": "success", "result": process.stdout}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Fabric command failed: {e.stderr}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))