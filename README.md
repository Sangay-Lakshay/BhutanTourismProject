# About
## Project
This project is about predicting the number of overnight visitors in Bhutan. The dataset is collected from the UN Data and had been preprocessed and cleaned. The model used for prediction is a Random Forest Regressor model. The model is trained on the dataset and the model is saved as a pickle file. The model is then loaded and used to predict the number of overnight visitors based on the user input.


## SetUp and Installation
- First start with installation of StreamLit on your device, please follow the steps for installation from [here](https://www.datacamp.com/tutorial/streamlit), if you dont have Anaconda install from [here](https://www.anaconda.com/download/success).
- Once your done with installation of StreamLit, clone this repository with the link for SSH or HTTPS in a folder of your choice using the following command.
    ```
    git clone LINK_HERE
    ```
- Install the modules that are required from the terminal where you setup your environment.
    ```
    cd PATH_TO_CLONED_FOLDER
    pip install requirement.txt
    ```
- To start the server use the following command:
    ```
    streamlit run main.py
    ```