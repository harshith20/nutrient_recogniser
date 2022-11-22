# nutrient_recogniser
Identify the name and nutrient facts ,by uploading pic of a vegetable or fruit

# Table of Contents

1. [Objective](#Objective)
2. [Ml_algo](#Ml_algo)
3. [Web_scrapping](#Web_scrapping)
4. [Backend](#Backend)




## Objective

My motive was to develop an application where i can click a pic of fruit or vegetable and get to know its name and nutrients of it


## Data
  collected data from kaggle 
   https://www.kaggle.com/datasets/moltean/fruits
      
                       
 ## ML_Algo
 I have used  tensorflow  neural network model with pre fetch and autotune as i had large data to handle . Also resized and rescaled data 

Using tensorflow pre fetch and autotune reduces load on ram tremendously .

Used various image preprocessing methods 
Feature extraction , feature preprocessing using conv2d, max pooling
I have gone through kaggle course’s and youtube which made my job easy.

I’ve used data augmentation too for better classification
While using neural networks  it may learn to overfit and not work for test data , so its important to use methods like ‘drop out’ , ‘early stopping’ to prevent it.

I got an accuracy of over 90% for the  validation data 

 ## Web_scrapping
Now , i wanted to show nutrition value of the fruit or vegetable according to the label predicted by the model.
I’ve collected pics of all the nutritional values of  labeled fruits and vegetables , saved them in static folder

## Backend 

used flask and python and made it into a web app 




![image](https://user-images.githubusercontent.com/73159496/203374732-a9880af2-66e6-4747-87a8-46ae608a38a3.png)

