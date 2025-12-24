import os
import re
import argparse
import shutil

def clean_filenames(input_dir, output_dir):
    """
    Parses filenames in input_dir, removes numeric prefixes, and saves them to output_dir.
    """
    # Regex to match digit(s) followed by " - " at the start of the filename
    pattern = re.compile(r'^\d+ - ')
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    files = os.listdir(input_dir)
    processed_count = 0

    print(f"Input: {input_dir}")
    print(f"Output: {output_dir}\n")

    for filename in files:
        old_path = os.path.join(input_dir, filename)
        
        # We only want to process files, not directories
        if not os.path.isfile(old_path):
            continue

        # Check for pattern match
        match = pattern.match(filename)
        if match:
            # Create new filename by removing the matched prefix
            new_filename = filename[match.end():]
        else:
            # Keep original filename if no match
            new_filename = filename
            
        new_path = os.path.join(output_dir, new_filename)
        
        # Perform the operation
        try:
            # If input and output are different, we copy to preserve originals
            # If they are the same, we rename in place
            if os.path.abspath(input_dir) == os.path.abspath(output_dir):
                if filename != new_filename:
                    os.rename(old_path, new_path)
                    print(f"Renamed: '{filename}' -> '{new_filename}'")
                    processed_count += 1
            else:
                shutil.copy2(old_path, new_path)
                print(f"Copied & Renamed: '{filename}' -> '{new_filename}'")
                processed_count += 1
        except Exception as e:
            print(f"Failed to process '{filename}': {e}")

    print(f"\nDone! Processed {processed_count} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean filenames by removing 'xx - ' numeric prefixes.")
    parser.add_argument("input", help="The directory containing files to clean.")
    parser.add_argument("output", nargs="?", help="The directory to save cleaned files. Defaults to input directory if not specified.")
    
    args = parser.parse_args()
    
    # If output is not provided, use input directory (in-place renaming)
    output_directory = args.output if args.output else args.input
    
    clean_filenames(args.input, output_directory)
