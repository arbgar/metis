![](https://github.com/arbgar/metis/blob/main/Deep%20Learning/Project/Deliverable/dl_picture.png?raw=true)

 *Photo by [Guido Blokker](https://unsplash.com/@gblokker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/mushroom?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

# Mining Magnificent Mushrooms

[The Mushroom Council](https://www.mushroomcouncil.com/nutrition-benefits/) highlights the many benefits of mushrooms, long considered one of the superfoods we should incorporate in our diet. Mushrooms are,

- Made up of cancer inhibiting compounds,
- Rich in antioxidants to support a healthy immune system,
- Low-energy-dense foods to manage weight, and
- Umami flavored to reduce need for sodium.

Unfortunately, mushrooms can also be highly toxic resulting in illness and even death.

There are millions of mushroom species and [about 14,000 described species](https://en.wikipedia.org/wiki/Mushroom). Of those, [just over 600 are on more than one continent and thought to be edible](https://ift.onlinelibrary.wiley.com/doi/full/10.1111/1541-4337.12708). Readily available in nature, even in urban settings, and beautiful, it is tempting harvest them for dinner.

**But how do you know, delectable or dangerous?**

## Design

This project will develop a visual mushroom classifier using Convolutional Neural Networks. The classifier could be used to identify wild mushrooms found during an urban hike. This classification could be a first step in understanding if the mushrooms are edible.

Not knowing much about mushrooms and wanting to use just a subset of the dataset described in the next section, I chose a binary classification of **edible** and **poisonous**. While not classifying the mushrooms by Genus and Species limited the dataset, it unfortunately also limited the model's ability to learn.  Because toxicity can vary within the Genus, it was very difficult for the classifier to detect image differences that correspond to toxicity.

I was curious what I could achieve despite this challenge, so I attempted a variety of models with largely the same result as flipping a coin.  I've concluded that the proper design for this problem is to classify by Genus and Species and then map to toxicity.  That said, I did learn quite a bit about deep learning models.

## Data

To begin this project, I selected the [University of Copenhagen, Natural History Museum of Denmark Fungi Classification Challenge](https://snm.ku.dk/english/news/all_news/2018/2018.5/the-fungi-classification-challenge/) dataset.  As described in the challenge, the dataset consists of 1,394 wild mushrooms species:

- 85,578 training images,
- 4,182 validation images, and
- 9,758 test set images.

Because my focus is on edible / poisonous mushrooms instead of the specific classification of mushrooms, I selected a subset of the available training / validation images to best illustrate the binary [edible](https://en.wikipedia.org/wiki/Edible_mushroom) / [poisonous](https://en.wikipedia.org/wiki/List_of_poisonous_fungus_species) classes. Using this approach, I collected the following images:

- Training: 6159 images belonging to 2 classes.
- Validation: 1539 images belonging to 2 classes.

## Algorithms

Starting small, I pre-processed the dataset to a standard 32 x 32-pixel image in grayscale.  Using this dataset, I developed a Random Forest Classifier with a training accuracy approaching 1.0 and a ROC of 0.588. The model was not correctly capturing key features.

Starting small to establish a modeling framework, I then set-up the following CNN:

- Input Layer: 150 x 150 pixels
- 2D Convolutional Layer: 32 filters, kernel size of 3, ReLU activation
- 2D Max Pooling Layer
- Flatten Layer
- Dense Layer: 64 nodes, ReLU activation, dropout 0.5
- Final Output Layer: 1 node, Sigmoid activation
- Compile: Binary Cross Entropy loss, RMSprop optimizer, and accuracy metrics
- Fit: 10 epochs with 100 steps per epoch

The small amount of data and limited iterations allowed fast model execution to work out the approach. This yielded a result slightly better than a guess with 61% accuracy. I then set-up a transfer model with a VGG16 base model and similar layers. This reduced the accuracy to 58% indicating that more data was needed.

From this point I increased the data and epochs.  I attempted a variety of models and parameters to develop a model that learns, but without much success.  The various architectures and parameters are summarized below. Loss was Binary Cross Entropy and I used both RMSprop and Adam Optimizers

| **Layer**                           | Output                | Transfer Learning  |
| ----------------------------------- | --------------------- | ------------------ |
| Input  (32 and 256 batch generator) | (None,  256, 256, 3)  |                    |
| 2D  Convolution (3,3)               | (None,  254, 254, 32) | VGG16 and ResNet50 |
| Activation  (ReLU)                  | (None,  254, 254, 32) | VGG16 and ResNet50 |
| 2D  MaxPooling                      | (None,  127, 127, 32) | VGG16 and ResNet50 |
| 2D  Convolution (3,3)               | (None,  125, 125, 32) | VGG16 and ResNet50 |
| Activation  (ReLU)                  | (None,  125, 125, 32) | VGG16 and ResNet50 |
| 2D  MaxPooling                      | (None,  62, 62, 32)   | VGG16 and ResNet50 |
| 2D  Convolution (3,3)               | (None,  60, 60, 64)   | VGG16 and ResNet50 |
| Activation  (ReLU)                  | (None,  60, 60, 64)   | VGG16 and ResNet50 |
| 2D  MaxPooling                      | (None,  30, 30, 64)   | VGG16 and ResNet50 |
| Flatten                             | (None,  57600)        |                    |
| Dense                               | (None,  64)           |                    |
| Activation  (ReLU)                  | (None,  64)           |                    |
| Dropout (0.5)                       | (None,  64)           |                    |
| Dense                               | (None,  1)            |                    |
| Activation  (Sigmoid)               | (None,  1)            |                    |

## Tools

- Pandas and Numpy for analysis
- Python glob and Pillow for file manipulation
- TensorFlow Keras for image pre-processing and modeling
- scikit-learn for modeling and measurement
- Matplotlib and Seaborn for visulatization

## Communication

The *Mining Magnificent Mushrooms* presentation summarizes the findings in graphical format including the following key elements:

- **The Case for Foraging ** which introduces the health importance of mushrooms and overviews varieties and foraging.
- **Answering the Question** which overviews the dataset and introduces the binary classification problem of edible or poisonous. It also alludes to the difficulty with this modeling design pattern.
- **Classification Process** which decribes the modeling including architectures and parameters.
- **Delectable or Dangerous** which summarizes the modeling results.
- **Regional Topics** which samples top topics by sub-region including polarity
- **Conclusions and Next Steps** which confirms the modeling design flaw and introduces an improved approach.

