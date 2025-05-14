Python script for opening zarr files via xarray straight into IPython session.

- Can be made an executable by `chmod +x path/to/zarr_interact/open_zarr.py` 
- Then by adding `path/to/zarr_interact/open_zarr.py` to a directory in `PATH` or by adding `path/to/zarr_interact/` to `PATH` to be run in any directory on machine. 

Can either be used interactively by simply calling `open_zarr.py` and choosing which file in current directory to open, or by e.g. `open_zarr.py path/to/zarr_file.zarr`.

Also imports `pyplot` from `matplotlib` (as `plt`) as standard for quick visualisation.