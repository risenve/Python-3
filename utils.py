import os

def create_folder(path):
    """Create a folder if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def list_director(path, do_print=True):
     """Return and print directory contents"""
     if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return []

    contents = os.listdir(path)
    if do_print:
        print(f"Contents of '{path}':")
        if not contents:
            print("  (empty)")
        else:
            for item in contents:
                print("  " + item)
        return contents

def create_text_file(folder, filename, text):
    """Create a text file safely inside a folder."""
    if not os.path.exists(folder):
        print(f"Cannot create file — folder does not exist: {folder}")
        return

    path = os.path.join(folder, filename)

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"File created: {path}")
    except Exception as e:
        print(f"Error creating file: {e}")
    
    def delete_file(folder, filename):
        """Delete a file safely from a folder."""
        path = os.path.join(folder, filename)

        if not os.path.exists(path):
            print(f"Cannot delete file — file does not exist: {path}")
            return

        try:
            os.remove(path)
            print(f"File deleted: {path}")
        except Exception as e:
            print(f"Error deleting file: {e}")

