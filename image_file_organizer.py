import os
import shutil

def organize_images():
    print("\n[Task 1] Image File Organizer")
    print("-" * 40)
    
    # Check multiple possible source folders
    possible_folders = ["images", "Initial_images", "Images", "initial_images"]
    source = None
    
    # Find which folder exists and has files
    for folder in possible_folders:
        if os.path.exists(folder) and os.path.isdir(folder):
            files = os.listdir(folder)
            if len(files) > 0:
                source = folder
                break
    
    # If no folder found, create default
    if source is None:
        source = "images"
        if not os.path.exists(source):
            os.makedirs(source)
            print("Created folder: " + source)
            print("Please add some images to organize.")
            return
    
    destination = "Organized_Images"
    
    # Get all files from source
    files = os.listdir(source)
    
    if len(files) == 0:
        print("No files found in '" + source + "' folder")
        print("Please add some images to organize.")
        return
    
    # Create destination if not exists
    if not os.path.exists(destination):
        os.makedirs(destination)
        print("Created folder: " + destination)
    
    # Supported image extensions
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', 
                  '.webp', '.tiff', '.tif', '.svg', '.ico']
    
    moved = 0
    skipped = 0
    
    print("\nProcessing " + str(len(files)) + " files from '" + source + "' folder...")
    print("-" * 40)
    
    for filename in files:
        file_path = os.path.join(source, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
        
        # Get extension (lowercase)
        ext = os.path.splitext(filename)[1].lower()
        
        # Check if image
        if ext in extensions:
            dest_path = os.path.join(destination, filename)
            
            # Handle duplicate names
            counter = 1
            while os.path.exists(dest_path):
                name, ext2 = os.path.splitext(filename)
                new_name = name + "_" + str(counter) + ext2
                dest_path = os.path.join(destination, new_name)
                counter += 1
            
            # Move file
            shutil.move(file_path, dest_path)
            moved += 1
            print("  Moved: " + filename)
        else:
            skipped += 1
            print("  Skipped: " + filename + " (not an image)")
    
    # Summary
    print("-" * 40)
    print("SUMMARY:")
    print("  Images moved: " + str(moved))
    print("  Files skipped: " + str(skipped))
    print("  Source: " + source + "/")
    print("  Destination: " + destination + "/")
    print("-" * 40)
    
    # Show moved files
    if moved > 0 and os.path.exists(destination):
        dest_files = os.listdir(destination)
        print("\nFiles in " + destination + "/:")
        for f in dest_files:
            print("  - " + f)

if __name__ == "__main__":
    organize_images()