from main_file import rename_file
from datetime import datetime

def test_rename_file():
    # Mock current date for testing purposes
    mock_date = datetime.now() # Replace with any date you want to test
    expected_file_name = f'TMOC_UTS_{mock_date.strftime("%Y%m%d")}.xlsx'

    # Call the function
    actual_file_name = rename_file()

    # Assert that the returned file name matches the expected format
    assert actual_file_name == expected_file_name
