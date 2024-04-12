# Skeleton ML Pipeline for Binvox Labels with AdditiveParts Dataset

This is a skeleton pipeline for training a machine learning model on the AdditiveParts dataset. The pipeline is designed to be run on a local machine, but can be easily adapted to run on a cloud-based machine.

Only a handful of binvox files are included in this repository. You will need to copy over the desired dataset files to the `data` directory under a similar naming system, where the parent folder is the Google Drive folder ID and the filenames are the model IDs as specified in `id_data.csv`.

Note that for the purposes of this demo, there is no `.gitignore` file for the `data` folder so that this works out-of-the-box, but in a real-world scenario, you would want to add this to your `.gitignore` file.