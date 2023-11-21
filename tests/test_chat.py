import pytest
from unittest.mock import patch, MagicMock, call
from src.chat import run_chat

@pytest.fixture(autouse=True)
def mock_qa():
    with patch('src.chat.qa') as mock_qa:
        # Mock qa function to return a specific response for 'exit'
        def qa_side_effect(question):
            if question["question"] == "exit":
                raise StopIteration  # Simulate breaking out of the loop
            return {"answer": "mocked answer"}

        mock_qa.side_effect = qa_side_effect
        yield mock_qa

@patch('builtins.input', side_effect=['A sample question', 'exit'])
@patch('builtins.print')
def test_run_chat(mock_print, mock_input, mock_qa):
    with pytest.raises(StopIteration):
        run_chat()

    # Check the actual calls
    expected_calls = [call("Ask any question regarding The Four Corners in California book:"),
                      call("mocked answer")]
    mock_print.assert_has_calls(expected_calls, any_order=False)

    # Check that qa was called with the expected input
    mock_qa.assert_any_call({"question": "A sample question"})
