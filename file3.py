with open('data.txt') as file:
    file.tell()
    print(f'Current file position is: {file.tell()}')
    print(file.read(4))
    file.tell()
    print(f'Position now is: {file.tell()}')
    file.seek(10, 0)
    print(f'New file position is: {file.seek(10, 0)}')

"""Creating a tool that manages files and directories, including writing functions.
Create a file search function to search for files within directories and sub directories based on name or file type.
Analyze file type and provide statistics on type distribution.
Navigate through directories by listing files within directories, changing and creating new directories.
Implement function to carry out operations like moving, copying, renaming and deleting files."""


def file_search(file_name, directory, sub_direct, checkdirectory, checksub):
    #checking if the file is in the directory and subdirectory
    if checkdirectory == 'Yes' and checksub == 'Yes':
        print(f'The file, {file_name} is in the directory. {directory} and subdirectory, {sub_direct}.')

    elif checkdirectory == 'Yes' and checksub == 'No':
        print(f'The file, {file_name} is in the directory. {directory} but not in the subdirectory, {sub_direct}.')
    
def file_analysis(file_name, file_short):

    #based on the file type and name
    if checkdirectory == 'Yes' and checksub == 'Yes':    
        if file_name == f'{file_short}.PNG':
            print(f'This file is also an image file in {sub_direct} subdirectory/package')
        elif file_name == f'{file_short}.mp4':
            print(f'This is also a video file in {sub_direct} subdirectory/package')
        elif file_name == f'{file_short}.doc' or file_name == f'{file_short}.pdf':
            print(f'This is also a document file in {sub_direct} subdirectory/package')
        elif file_name == f'{file_short}.py':
            print(f'This is also a module/python script in {sub_direct} subdirectory/package')
                      
def directory_navigation(directory, newdirectory, alternative_dir_name):
    #creating new directory
    import shutil
    shutil.copytree(f'{directory}', f'{newdirectory}')
    
    #changing directory
    import os
    os.rename(f'{directory}', f'{alternative_dir_name}')
    
    #list of files present in directory
    file_list = []
    if checkdirectory == 'Yes' and checksub == 'Yes':
        file_list.append(file_name)

def file_operations(directory, sub_direct, newdirectory, file_name, new_file_name):

    #copying and moving files
    import shutil
    shutil.copy(f'{directory}/{sub_direct}/{file_name}', f'{newdirectory}/{file_name}')
    shutil.move(f'{directory}/{sub_direct}/{file_name}', f'{newdirectory}/{file_name}')

    #deleting and renaming
    import os
    os.rename(f'{directory}/{sub_direct}/{file_name}',f'{directory}/{sub_direct}/{new_file_name}')
    os.remove(f'{directory}/{sub_direct}/{file_name}')


performance = True        
while performance is True:
    file_name = input('Please enter the name of the file: ')
    if file_name == 'done':
        break
    else:
        file_short = input('Please enter the file name without extension: ')
        directory = input('Please enter the name of the directory: ')
        sub_direct = input('Please enter the name of the subdirectory: ')
        checkdirectory = input(f'Is the file, {file_name} in the directory {directory}? ')
        checksub = input(f'Is the file, {file_name} in the subdirectory {sub_direct}? ')
        print('')
        print('For the function, directory navigation: ')
        print('')

        newdirectory = input('Enter new name for new directory: ')
        alternative_dir_name = input('Enter alternative name for directory renaming: ')     
        print('')
        print('For the function, file operations: ')
        print('')

        new_file_name = input('Enter new name for file: ')
        print('')
        print('To continue....')
        
        #counting the number of documents, images, videos and modules
        count_img = 0
        count_vid = 0
        count_doc = 0
        count_py = 0
        if file_name == f'{file_short}.PNG':
            count_img += 1
        elif file_name == f'{file_short}.mp4':
            count_vid += 1
        elif file_name == f'{file_short}.doc' or file_name == f'{file_short}.pdf':
            count_doc += 1
        elif file_name == f'{file_short}.py':
            count_py += 1

        
        file_search(file_name, directory, sub_direct, checkdirectory, checksub)
        file_analysis(file_name, file_short)



print(f'There are {count_img} images in the directory {directory}')
print(f'There are {count_vid} videos in the directory {directory}')
print(f'There are {count_doc} documents in the directory {directory}')
print(f'There are {count_py} modules/python scripts in the directory {directory}')




