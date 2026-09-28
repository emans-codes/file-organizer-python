import os 

folder_path = input("Enter the folder path : ").strip('"')

if not os.path.isdir(folder_path):
    print("Folder not found. Please check the path and try again.")
    exit()

files = os.listdir(folder_path)
organized_count = 0

print("\nStarting file organization...\n")

for file in files :
    if os.path.isfile(os.path.join(folder_path, file)):
        extension = os.path.splitext(file)[1]

        if extension :
            folder_name = extension[1:].upper()
            folder_path_new = os.path.join(folder_path, folder_name)
            os.makedirs(folder_path_new, exist_ok=True)

            destination = os.path.join(folder_path_new , file)

            if os.path.exists(destination) :
                name , extension = os.path.splitext(file)
                counter = 1

                while os.path.exists(destination) :
                    new_name = f"{name}_{counter}{extension}"
                    destination = os.path.join(folder_path_new, new_name)
                    counter += 1
            try :
                os.rename(
                    os.path.join(folder_path, file),
                    destination
                )
                print(f"Organized: {file} → {folder_name}")
                organized_count += 1

            except OSError as error :
                print(f"Could not organize {file}: {error}")
        else :
            print(f"Skipped: {file} (no extension)")

print("\n================================")
print("     ORGANIZATION COMPLETE")
print("================================")
print(f"Files organized: {organized_count}")
print("================================")
