import os
def fileD():
    folder_path = 'uploaded_images/'
    if os.path.exists(folder_path):
        # iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            # check if it is a file (not a directory)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Remove the file
        # print(f"All files have been removed from {folder_path}.")
    else:
        # print(f"The folder {folder_path} does not exist.")
        pass
def rename():
    # Path to the folder
    folder_path = 'uploaded_images/'

    # List all files in the folder
    files = os.listdir(folder_path)

    # Rename the first file to "image"
    # for file in files:
    #     old_file_path = os.path.join(folder_path, file)
    #     new_file_path = os.path.join(folder_path, "image" + os.path.splitext(file)[1])  # Preserve the original extension
    for file in files:
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, "image.png")  # Set new name with .png extension
        # Rename the file
        os.rename(old_file_path, new_file_path)
        # print(f"Renamed {file} to {os.path.basename(new_file_path)}")
        
        break  # Stop after renaming the first file
    return new_file_path