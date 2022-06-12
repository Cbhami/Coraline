#import libraries
import os
from pathlib import Path
#Dictionary (Add more if you want)
DIRECTORIES = {
    'html': ['.html5', '.html', '.htm', '.xhtml'],
    'pbix' : ['.pbix', '.pbit'],
    'images': ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', 'svg',
               '.heif', '.psd'],
    'videos': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng',
               '.qt', '.mpg', '.mpeg', '.3gp', '.mkv'],
    'documents': ['.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox',
                  '.rvg', '.rtf', '.rtfd', '.wpd', '.ppt',
                  'pptx'],
    'workbooks' : ['.xls', '.xlsx'],
    'csv data' : ['.csv'],
    'ppt' : ['.ppt', '.pptm', '.pptx'],
    'archives': ['.a', '.ar', '.cpio', '.iso', '.tar', '.gz', '.rz', '.7z',
                 '.dmg', '.rar', '.xar', '.zip'],
    'audio': ['.aac', '.aa', '.aac', '.dvf', '.m4a', '.m4b', '.m4p', '.mp3',
              '.msv', 'ogg', 'oga', '.raw', '.vox', '.wav', '.wma'],
    'plaintext': ['.txt', '.in', '.out'],
    'pdf': ['.pdf'],
    'python': ['.py'],
    'xml': ['.xml'],
    'exe': ['.exe'],
    'shell': ['.sh'],
    'r': ['.r', '.rmd'],
    'jupyter' : ['.ipynb']
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
#This will organise your files
def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
   #if extension not present in the dctionary than create a folder name 'OTHER'
    try:
        os.mkdir('OTHER')
    except:
        pass
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER/' + str(Path(dir)))
        except:
            pass
if __name__ == '__main__':
    organize()