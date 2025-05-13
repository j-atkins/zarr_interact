#!/usr/bin/env python

import os
import glob
import subprocess
import argparse


def open_zarr_with_xarray_in_ipython(zarr_path):
    """Opens the specified Zarr store using xarray in an interactive IPython session."""
    try:
        command = f"ipython -i -c \"import xarray as xr; ds = xr.open_zarr('{zarr_path}'); print(f'Opened Zarr dataset: {{ds}}'); print('Zarr dataset \\'ds\\' is now available. Keep this IPython session running to explore.')\""
        subprocess.run(command, shell=True, check=True)
        print(
            f"Opened Zarr file: {zarr_path} with xarray in an interactive IPython session."
        )
    except FileNotFoundError:
        print(
            "Error: IPython not found. Please ensure it is installed and in your PATH."
        )
    except subprocess.CalledProcessError as e:
        print(f"Error opening {zarr_path} with xarray: {e}")


def find_zarr_files():
    """Finds all .zarr directories in the current directory."""
    return glob.glob("*.zarr")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Quickly open a .zarr file with xarray in an interactive IPython session."
    )
    parser.add_argument(
        "zarr_file", nargs="?", help="Path to a specific .zarr file to open."
    )
    args = parser.parse_args()

    if args.zarr_file:
        zarr_path = args.zarr_file
        if os.path.exists(zarr_path) and zarr_path.endswith(".zarr"):
            print(f"Attempting to open specified Zarr file with xarray: {zarr_path}")
            open_zarr_with_xarray_in_ipython(zarr_path)
        else:
            print(
                f"Error: Specified file '{zarr_path}' does not exist or is not a .zarr file."
            )
    else:
        zarr_files = find_zarr_files()

        if not zarr_files:
            print("No .zarr files found in the current directory.")
        elif len(zarr_files) == 1:
            zarr_path = zarr_files[0]
            print(f"Found one .zarr file: {zarr_path}")
            open_zarr_with_xarray_in_ipython(zarr_path)
        else:
            print("Found multiple .zarr files:")
            for i, path in enumerate(zarr_files):
                print(f"{i + 1}. {path}")

            while True:
                try:
                    choice = input(
                        "Enter the number of the .zarr file you want to open (or 'q' to quit): "
                    )
                    if choice.lower() == "q":
                        break
                    index = int(choice) - 1
                    if 0 <= index < len(zarr_files):
                        zarr_path = zarr_files[index]
                        open_zarr_with_xarray_in_ipython(zarr_path)
                        break
                    else:
                        print("Invalid selection. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'q'.")
