#!/usr/bin/python

import cgi
import json
import logging
from urllib.request import urlopen
import papermill
from pathlib import Path


def download_notebook_from_gdrive(notebook_id):
    notebook_url = f'https://drive.google.com/uc?id={notebook_id}&export=download'

    # download notebook
    response = urlopen(notebook_url)
    notebook_dict = json.loads(response.read())

    # extract notebook name
    _, params = cgi.parse_header(response.headers.get('Content-Disposition', ''))
    notebook_name = params['filename']

    # set parameters tag
    notebook_dict['cells'][0]['metadata']['tags'] = ['parameters']

    # specify the kernel language
    notebook_dict['metadata']['kernelspec']['language'] = 'python'

    # save notebook
    f = open('notebooks/'+notebook_name, "w")
    json.dump(notebook_dict, f)
    f.close()

    return notebook_name


Path("notebooks/").mkdir(parents=True, exist_ok=True)
Path("results/").mkdir(parents=True, exist_ok=True)

notebook_link = 'https://colab.research.google.com/drive/18kKHO2KYePa-mTbQDZADMkBlydFOX9u0?usp=sharing'
notebook_id = notebook_link.split("/")[4].split("?")[0]
notebook_name = download_notebook_from_gdrive(notebook_id)

# A sample for the FLAN-T5-Rep(En)-ClUn(En) approach on MPQA Intensity
experiment_name = f"MPQA-I-Flan-T5-RepEn-ClUnEn"
papermill.execute_notebook(
    input_path = f'notebooks/{notebook_name}',
    output_path = f'results/{experiment_name}_{notebook_name}',
    parameters = dict(
        RUNTIME_TYPE = 'CONDA', # Keep it as CONDA if running on anything other than Google Colab
        EXPERIMENT_NAME = experiment_name,
        DATASET_NAME = f'MPQA-I',
        BASE_MODEL = 'FLAN-T5',
        AFL_METHOD = "Rep(En)-ClUn(En)",
        SAMPLING_ITERATIONS = 10,
        NUMBER_OF_SAMPLES_PER_ITERATION = 10,
        REPEAT_SAMPLING = 5,
        STORE_RESULTS = ['eval_main_metric'],
        mpqa_i_train_link = '[Please Modify]',
        mpqa_i_val_link   = '[Please Modify]',
        mpqa_i_test_link  = '[Please modify]',
    )
)