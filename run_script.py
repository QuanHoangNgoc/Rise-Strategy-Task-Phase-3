import os
import subprocess
import sys


def run_python_script(script_path):
    try:
        # Check if script exists
        if not os.path.exists(script_path):
            print(f"Error: Script not found at {script_path}")
            return False

        # Run the script and capture output
        print(f"Running script: {script_path}")
        result = subprocess.run([sys.executable, script_path],
                                capture_output=True,
                                text=True)

        # Print the output
        if result.stdout:
            print("\nOutput:")
            print(result.stdout)

        # Print any errors
        if result.stderr:
            print("\nErrors:")
            print(result.stderr)

        # Check if script ran successfully
        if result.returncode == 0:
            print("\nScript completed successfully!")
            return True
        else:
            print(f"\nScript failed with return code: {result.returncode}")
            return False

    except Exception as e:
        print(f"An error occurred while running the script: {str(e)}")
        return False


if __name__ == "__main__":
    # Default script to run if no argument provided
    default_script = "convert_to_excel.py"

    # Get script path from command line argument or use default
    script_path = sys.argv[1] if len(sys.argv) > 1 else default_script

    # Run the script
    success = run_python_script(script_path)

    if not success:
        sys.exit(1)
