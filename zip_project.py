import os
import shutil
import zipfile
from datetime import datetime


def zip_current_folder(output_zip_name=None, exclude_patterns=None):
    """
    Zips the entire current directory into a zip file.

    Args:
        output_zip_name (str, optional): Name of the output zip file.
                                        Defaults to 'project_{date}.zip'.
        exclude_patterns (list, optional): List of patterns to exclude.
                                        Defaults to ['.git', '__pycache__', '*.zip'].

    Returns:
        str: Path to the created zip file
    """
    # ! Default excluded patterns
    if exclude_patterns is None:
        exclude_patterns = ['.git', '__pycache__', '.vscode'
                            '*.zip', '*.pyc', 'temp_*']

    # ! Default output name with timestamp
    if output_zip_name is None:
        date_str = datetime.now().strftime("%d_%H%M")
        output_zip_name = f"project_{date_str}.zip"

    # Get current directory
    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir)

    print(f"✅ Starting to zip current folder: {current_dir}")
    print(f"✅ Will exclude: {exclude_patterns}")

    # Create zip file
    with zipfile.ZipFile(output_zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_count = 0
        total_size = 0

        # Walk through directory
        for root, dirs, files in os.walk(current_dir):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if not any(
                pat in d for pat in exclude_patterns)]

            # Get relative path from current directory
            rel_path = os.path.relpath(root, current_dir)
            if rel_path == '.':
                rel_path = ''

            # Add files
            for file in files:
                # Skip excluded patterns
                if any(pat in file for pat in exclude_patterns):
                    continue

                file_path = os.path.join(root, file)
                # Get file size
                file_size = os.path.getsize(file_path)
                total_size += file_size

                # Add to zip using relative path
                archive_path = os.path.join(rel_path, file)
                zipf.write(file_path, archive_path)
                file_count += 1

                # Print progress for larger projects
                if file_count % 10 == 0:
                    print(f"✅ Zipped {file_count} files...")

    # Get final zip size
    zip_size = os.path.getsize(output_zip_name)
    zip_size_mb = zip_size / (1024 * 1024)
    total_size_mb = total_size / (1024 * 1024)

    print(f"\n✅ Zip completed successfully!")
    print(f"✅ Total files zipped: {file_count}")
    print(f"✅ Original size: {total_size_mb:.2f} MB")
    print(f"✅ Compressed size: {zip_size_mb:.2f} MB")
    print(f"✅ Compression ratio: {zip_size/total_size:.2f}")
    print(f"✅ Zip file created at: {os.path.abspath(output_zip_name)}")

    return output_zip_name


if __name__ == "__main__":
    try:
        # You can customize the zip file name and exclusion patterns here
        zip_file = zip_current_folder()
        print(f"✅ Successfully created {zip_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
