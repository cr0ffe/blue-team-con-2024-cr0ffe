import os
import shutil
import subprocess
import sys

# Author: Jeremy Peters @ SentryWire

def generate_shortcuts(url: str, separator: str = '/tree', cwd: str = None):
    if not cwd:
        cwd = os.getcwd()

    split_url = url.split(separator)

    # Folder path to download from
    folder_path = split_url[1]

    # Create folder for files to be cloned into
    download_folder_name = str(folder_path.split('/')[-1])
    download_folder_path = os.path.join(cwd, download_folder_name)
    
    # Download everything in this folder
    folder_path += '/*'
    folder_path = '/'.join(folder_path.split('/')[2:])

    # Append .git to the URL to make it functional
    git_url = f"{split_url[0]}.git"

    # Sparse path config stuff
    info_path = os.path.join(download_folder_path, '.git', 'info')
    sparse_checkout_path = os.path.join(info_path, 'sparse-checkout')

    return {
        'git_url': git_url,
        'folder_path': folder_path,
        'download_folder_name': download_folder_name,
        'download_folder_path': download_folder_path,
        'info_path': info_path,
        'sparse_checkout_path': sparse_checkout_path
    }

def cleanup_git(download_folder_path: str):
    subprocess.check_call(['rm', '-rf', '.git'], cwd=download_folder_path)

def cleanup_empty(download_folder_path: str, folder_path: str):
    subprocess.check_call(['rm', '-rf', folder_path.split('/')[0]], cwd=download_folder_path)

def git_init(download_folder_name: str, cwd: str) -> None:
    subprocess.check_call(['git', 'init', download_folder_name], cwd=cwd)

def git_add_remote(download_folder_path: str, git_url: str) -> None:
    subprocess.check_call(['git', 'remote', 'add', 'origin', git_url], cwd=download_folder_path)

def git_sparse_config(download_folder_path: str) -> None:
    subprocess.check_call(['git', 'config', 'core.sparseCheckout', 'true'], cwd=download_folder_path)

def configure_sparse(info_path: str, sparse_checkout_path: str, folder_path: str) -> None:
    os.makedirs(info_path, exist_ok=True)
    with open(sparse_checkout_path, 'w') as file:
        file.write(folder_path)

def git_fetch(download_folder_path: str) -> None:
    subprocess.check_call(['git', 'fetch', '--depth=1', 'origin', 'main'], cwd=download_folder_path)

def git_checkout(download_folder_path: str) -> None:
    subprocess.check_call(['git', 'checkout', 'main'], cwd=download_folder_path)

def collapse_nested(download_folder_path: str) -> None:
    for root, dirs, files in os.walk(download_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, download_folder_path)

def main(url: str) -> None:
    cwd = os.getcwd()

    shortcuts = generate_shortcuts(url)

    try:
        cleanup_git(shortcuts['download_folder_path'])
    except FileNotFoundError:
        pass

    print("Initializing GIT")
    git_init(shortcuts['download_folder_name'], cwd)

    print("Adding Remote Repo")
    git_add_remote(shortcuts['download_folder_path'], shortcuts['git_url'])

    print("Configuring Sparse Checkout")
    git_sparse_config(shortcuts['download_folder_path'])
    configure_sparse(shortcuts['info_path'], shortcuts['sparse_checkout_path'], shortcuts['folder_path'])
    
    print("Fetching Files")
    git_fetch(shortcuts['download_folder_path'])
    git_checkout(shortcuts['download_folder_path'])

    print("Cleaning GIT")
    cleanup_git(shortcuts['download_folder_path'])

    print("Collapsing Nested Folders")
    collapse_nested(shortcuts['download_folder_path'])
    cleanup_empty(shortcuts['download_folder_path'], shortcuts['folder_path'])

    print("Done!")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)
    
    URL = sys.argv[1]
    main(URL)
