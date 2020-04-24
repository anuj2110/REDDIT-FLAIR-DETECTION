# Reddit Flair Detector
---
A web app to predict reddit flairs of India subredit posts by the url(s) provided by the users using Machine Learning algorithms. [This is the web app link] and [this is the automated_testing link]

## Important Files and Directories
The main directory is a **django application** hosted on **heroku**. The important directories and files are as follows:
- [media]: This folder is used to store the uploaded text file (from automated_testing route) for reading the urls.

- [Notebooks and data](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/Notebooks%20and%20data/): This directory contains the notebooks,data collected from reddit and trained ml models.

- [Notebooks and data/Notebooks](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/Notebooks%20and%20data/Notebooks): This directory contains all the notebooks used in this project.

- [Notebooks and data/models](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/Notebooks%20and%20data/models): This directory contains trained ml models and the preprocessor for them in .sav file format.

- [Notebooks and data/train_testdata](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/Notebooks%20and%20data/train_testdata): This directory contains the data collected in train-test splits to get the same results.

- [reddit_flair_detector](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/reddit_flair_detector): The directory for the web app which uses machine learning models and shows/sends the results.

- [manage.py](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/blob/master/manage.py): The file to run the server.

- [webapp](https://github.com/anuj2110/REDDIT-FLAIR-DETECTION/tree/master/webapp): Contains the setting and config files for reddit_flair_detector.

## Steps to execute project
- Clone the repository in your system.
- cd into repository folder.
- Create a virtual environment using Anaconda/virtualenv and activate it.
- Run the command **pip install -r requirements.txt**.
- To start the server execute **python manage.py runserver**
- After start it will provide the IP address. Copy this and paste it in the web browser.
- For **automated testing**:
  - The required key for automated testing is **upload_file**
  - The url for automated testing after running locally will be (example) **http://127.0.0.1:8000/automated_testing**
  
## Important Packages:
- Praw
- numpy
- pandas
- matplotlib
- scikit-learn
- django
- Seaborn



