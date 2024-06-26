# Poem_Pulse

## Overview 

In this project, I ventured into the realm of generative AI development by creating a poem summarizer. Leveraging NLP and deep learning techniques, I utilized the power of Hugging Face Transformers. The project encompassed various stages, from data collection to model deployment and API integration.

Data collection was facilitated through Selenium web scraping techniques, enabling the compilation of a comprehensive dataset with the assistance of Hugging Face Transformers. The model itself was trained using Transformers models, with initial deployment conducted on Hugging Face Spaces.

To ensure accessibility and usability, I further integrated the model into a Flask application, leveraging the Hugging Face API.


## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Data Collection](#data-collection)
- [Model Training](#data-modelling)
- [HuggingFace Deployment](#huggingface-deployment)



## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/marufc36/Poem_Pulse.git
   ```
  
## Dependencies
   ```bash
pip3 install requirements.txt
```


## Data Collection 


Data was collected from the [Poets.org](https://poets.org/) using Selenium. Initially, I collected all links for poems using web scraping techniques. Afterward, I scraped poems along with their names using the previously gathered links. However, the challenge arose when creating summaries for each poem. To tackle this, I employed the facebook/bart-large-cnn model.

My dataset was fed into the model loop, generating a summary for each poem, which was then saved into a Pandas dataframe. Approximately 15,000 poems were scraped, resulting in a poem dataset with summaries comprising 5,296 poems. To maintain traceability throughout my working process, I had to split my link dataset.


## Model Training

The model was trained on the t5-base transformer model. I utilized the T5TokenizerFast for tokenizing purposes. The dataset was narrowed down to two columns: 'Poem Content' and 'Jist' (the summary of the poems). The dataset was split into train_df and test_df, where train_df contained 4,766 poems and test_df contained 530 poems.

The model underwent training for 3 epochs, and the best model, determined by the lowest validation loss, was saved as a model checkpoint.

Also I have quantized the model for faster inference.





## HuggingFace Deployment
Model was initially deployed into huggingface spaces. 

https://huggingface.co/spaces/mmchowdhury/PoemPulse



![alt text](image.png)



