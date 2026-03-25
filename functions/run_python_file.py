import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_path,file_path))
        val_dir = os.path.commonpath([abs_working_path, target_dir]) == abs_working_path
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        if not val_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        
        command = ["python", target_dir]
        if args is not None:
            command.extend(args)
        result = subprocess.run(command, capture_output=True,timeout=30.0,text=True)
        
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not (result.stderr or result.stdout):
            return "No output produced"
        return f"""STDOUT: {result.stdout}\nSTDERR: {result.stderr}"""

    except Exception as e:
        return f"Error: error opening a python script: {e}"    
