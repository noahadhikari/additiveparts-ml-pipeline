# Skeleton ML Pipeline for Binvox Labels with AdditiveParts Dataset

This is a skeleton pipeline for training a machine learning model on the AdditiveParts dataset. The pipeline is designed to be run on a local machine, but can be easily adapted to run on a cloud-based machine.

Only a handful of binvox files are included in this repository. You will need to copy over the desired dataset files to the `data` directory under a similar naming system, where the parent folder is the Google Drive folder ID and the filenames are the model IDs as specified in `id_data.csv`.

Note that for the purposes of this demo, there is no `.gitignore` file for the `data` folder so that this works out-of-the-box, but in a real-world scenario, you would want to add this to your `.gitignore` file.

## Overview

There is a PyTorch dataloader for converting the binvox files into 3D arrays, which is configured to ignore parts that aren't found on disk or that do not have a valid rating. The model is a simple flattened fully connected network, outputting five labels for the manual labels (-2 to 2) or a single scalar value for the Tweaker3 labels.

To run the model on the manual labels, run `python model_for_manual_labels.py`. To run the model on the Tweaker3 labels, run `python model_for_tweaker_labels.py`.