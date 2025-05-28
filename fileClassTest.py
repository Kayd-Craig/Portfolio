from file import File
import pytest
from pathlib import Path

def test_get_name(tmp_path):
    
    temp_file = tmp_path / "new_text.txt"
    temp_file.write_text("Temporary content")  
    
   
    file_instance = File(str(temp_file))
    
    
    assert file_instance.get_name() == "new_text.txt"

def test_get_contents(tmp_path):
    
    test_content = "Hello, this is test content."
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text(test_content)  # Write the content to the file
    
    
    file_instance = File(str(temp_file))
    
    assert file_instance.get_contents() == test_content

def test_save_file(tmp_path):
    
    path = tmp_path / "save_test.txt"
    contents = "Sample content for testing save_file"
    
    
    file_instance = File(str(path), contents)
    
    
    file_instance.save_file()
    
    
    saved_contents = path.read_text()
    
    
    assert saved_contents == contents
