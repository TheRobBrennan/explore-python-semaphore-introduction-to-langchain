import subprocess
import pytest
from pathlib import Path

@pytest.fixture
def chat_script_path():
    # Assuming the chat.py script is in the src directory
    return Path(__file__).parent.parent / "src" / "chat.py"

def test_run_chat_as_main(chat_script_path):
    # Run the chat.py script as a standalone script
    result = subprocess.run(["python", chat_script_path], capture_output=True, text=True, input="exit\n")

    # Check if the script started correctly
    assert "Ask any question regarding The Four Corners in California book:" in result.stdout

    # You can add more assertions here based on the expected behavior of your script
