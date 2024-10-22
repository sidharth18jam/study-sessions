import os
import zipfile

# 1. Input: folder paths
zip_folder = '/Users/sid/google backup'
output_folder = '/Users/sid/Photos'

# 2. Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Function to find a unique file name in case of conflict
def get_unique_file_path(directory, file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1
    new_file_name = file_name
    new_file_path = os.path.join(directory, new_file_name)
    
    # Keep modifying the file name until a unique one is found
    while os.path.exists(new_file_path):
        new_file_name = f"{base_name}_{counter}{extension}"
        new_file_path = os.path.join(directory, new_file_name)
        counter += 1
    
    return new_file_path

# 4. Iterate over all files in the given folder
for file_name in os.listdir(zip_folder):
    if file_name.endswith(".zip"):
        zip_file_path = os.path.join(zip_folder, file_name)
        
        # 5. Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # 6. Iterate over each file in the zip
            for member in zip_ref.infolist():
                try:
                    # 7. Skip directories
                    if member.is_dir():
                        continue

                    # 8. Skip files with .json extension
                    if member.filename.endswith(".json"):
                        continue

                    # 9. Determine the file extension (remove leading dot for folder name)
                    file_extension = os.path.splitext(member.filename)[1][1:]

                    # 10. Create a subfolder based on the file extension
                    extension_folder = os.path.join(output_folder, file_extension)
                    if not os.path.exists(extension_folder):
                        os.makedirs(extension_folder)

                    # 11. Get the base file name (ignore the original folder structure)
                    base_file_name = os.path.basename(member.filename)

                    # 12. Check if a file with the same name exists, and rename if necessary
                    destination_path = get_unique_file_path(extension_folder, base_file_name)

                    # 13. Extract and save the file in the extension-based folder
                    with zip_ref.open(member) as source_file:
                        with open(destination_path, "wb") as target_file:
                            target_file.write(source_file.read())
                except Exception as e:
                    print(f"Failed to extract {member.filename}: {e}")

print("Extraction completed! All files categorized by extension and renamed if needed.")
