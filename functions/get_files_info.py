import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        
        if not valid_target_dir:
            return f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        items_in_dir = []
        for item in os.listdir(target_dir):
            filepath = os.path.join(target_dir, item)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            items_in_dir.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(items_in_dir)
    except Exception:
        return f"Error listing files: {Exception}"


