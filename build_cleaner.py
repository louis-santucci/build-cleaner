from pathlib import Path
from typing import List

import os, shutil

import click

__clean_ignore_filename__ = ".cleanignore"
__cleanable_filename__ = ".cleanable"

def read_file_to_list(filename: str) -> None:
    ignoreList = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                ignoreList.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    return ignoreList

def clean_folder(
        folder: str,
        cleanable: List[str] = [],
        ignore_list: List[str] = [],
        ignore: bool = False
        ) -> int:
    clean_counter = 0
    _, foldername = os.path.split(folder)
    if foldername not in ignore_list and foldername in cleanable:
        if not ignore:
            try:
                print(f"Removing {folder}")
                shutil.rmtree(folder)
                clean_counter += 1
            except OSError as o:
                print(f"Error, {o.strerror}: {folder}")
        else:
            print(f"Ignoring {folder}")
    else:
        listdir = os.listdir(folder)
        for file in listdir:
            path = os.path.join(folder, file)
            if not os.path.isfile(path):
                clean_counter += clean_folder(path, cleanable, ignore_list, ignore or file in ignore_list)
    return clean_counter
            

@click.command()
@click.option(
    "-r",
    "--root",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=None
    ),
    show_default=True,
    default=".")
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
)
def cli(paths: str, root: str) -> None:
    ignore_list = read_file_to_list(os.path.join(root, __clean_ignore_filename__))
    print(f"Ignore following folder names: {ignore_list}")
    to_clean_list = read_file_to_list(os.path.join(root, __cleanable_filename__))
    print(f"Clean following folder names: {to_clean_list}")
    print("---")
    for i, path in enumerate(paths):
        if len(paths) > 1:
            click.echo(f"{path}:")
        
        count = clean_folder(path, to_clean_list, ignore_list)
        print("---")
        print(f"Cleaned {count} folder(s) in {path}")
        if i < len(paths) - 1:
            click.echo("\n")
        else:
            click.echo()

if __name__ == "__main__":
    cli()