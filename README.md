<h1 align=center style="margin:100"> Active Few-Shot Learning for Text Classification </h1>
<p align=center> <i> The 2025 Annual Conference of the Nations of the Americas Chapter of the ACL (NAACL 2025) </i> </p>
<p align=center>
  <a href="https://scholar.google.com/citations?user=Sy04BWcAAAAJ">Saeed Ahmadnia</a> &emsp;
  <a href="https://scholar.google.com/citations?user=HLM9w-sAAAAJ">Arash Yousefi Jordehi</a> &emsp;
  <a href="https://scholar.google.com/citations?user=s1dtXCIAAAAJ">Mahsa Hosseini Khasheh Heyran</a>
  <br>
  <a href="https://scholar.google.com/citations?user=WGH3eIsAAAAJ">Seyed Abolghasem Mirroshandel</a> &emsp;
  <a href="https://scholar.google.com/citations?user=AWNL69MAAAAJ">Owen Rambow</a> &emsp;
  <a href="https://scholar.google.com/citations?user=vkX6VV4AAAAJ">Cornelia Caragea</a>
</p>
<p align=center>
  <a href="https://arxiv.org/abs/2502.18782"><img src="https://img.shields.io/badge/arXiv-EC008C"/></a>
  <a href="https://arxiv.org/pdf/2502.18782"><img src="https://img.shields.io/badge/Paper-FC6767"/></a>
</p>

## Abstract
The rise of Large Language Models (LLMs) has boosted the use of Few-Shot Learning (FSL) methods in natural language processing, achieving acceptable performance even when working with limited training data. The goal of FSL is to effectively utilize a small number of annotated samples in the learning process. However, the performance of FSL suffers when unsuitable support samples are chosen. This problem arises due to the heavy reliance on a limited number of support samples, which hampers consistent performance improvement even when more support samples are added. To address this challenge, we propose an active learning-based instance selection mechanism that identifies effective support instances from the unlabeled pool and can work with different LLMs. Our experiments on five tasks show that our method frequently improves the performance of FSL.

<hr>

## Datasets
- [MPQA](https://github.com/theSaeed/opinion-mining-using-llms)
- [AG News (Kaggle)](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
- [Amazon Reviews (Kaggle)](https://www.kaggle.com/datasets/mexwell/amazon-reviews-multi)

## Usage

> [!NOTE] 
> The code is also hosted on [Google Colab](https://colab.research.google.com/drive/18kKHO2KYePa-mTbQDZADMkBlydFOX9u0) and can be executed directly without manually setting up the environment.

1. Create and activate the required environment:

```bash
conda env create -f afl-env.yml
conda activate afl-env
```

2. Modify the parameters in the first cell of the notebook as needed, either directly or in `main.py`.

> [!IMPORTANT] 
> Ensure that the datasets required for your experiments are prepared, and their link parameters are correctly set before proceeding.

3. Run the experiments:

```bash
python main.py
```

## Citation
If you find our method helpful or relevant to your work, please kindly cite the following paper:

```bibtex
@misc{ahmadnia2025activefewshotlearningtext,
      title={Active Few-Shot Learning for Text Classification}, 
      author={Saeed Ahmadnia and Arash Yousefi Jordehi and Mahsa Hosseini Khasheh Heyran and Seyed Abolghasem Mirroshandel and Owen Rambow and Cornelia Caragea},
      year={2025},
      eprint={2502.18782},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.18782}, 
}
```