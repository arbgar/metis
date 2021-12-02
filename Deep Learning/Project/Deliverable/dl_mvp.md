![](https://github.com/arbgar/metis/blob/main/Deep%20Learning/Project/dl_picture.png?raw=true)

*Photo by [Guido Blokker](https://unsplash.com/@gblokker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/mushroom?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

# Mining Magnificent Mushrooms

To begin this project, I selected the [University of Copenhagen, Natural History Museum of Denmark Fungi Classification Challenge](https://snm.ku.dk/english/news/all_news/2018/2018.5/the-fungi-classification-challenge/) dataset.  Because my focus is on edible / poisonous mushrooms instead of the specific classification of mushrooms, I selected a subset of the available training / validation images to best illustrate the binary [edible](https://en.wikipedia.org/wiki/Edible_mushroom) / [poisonous](https://en.wikipedia.org/wiki/List_of_poisonous_fungus_species) classes. Using this approach, I collected the following images:

- Training: 6159 images belonging to 2 classes.
- Validation: 1539 images belonging to 2 classes.

Starting small to establish a modeling framework, I set-up the following CNN:

- Input Layer: 150 x 150 pixels
- 2D Convolutional Layer: 32 filters, kernel size of 3, relu activation
- 2D Max Pooling Layer
- Flatten Layer
- Dense Layer: 64 nodes, relu activation, dropout 0.5
- Final Output Layer: 1 node, sigmoid activation
- Compile: binary_crossentropy, rmsprop optimizer, and accuracy metrics
- Fit: 10 epochs with 100 steps per epoch

The small amount of data and limited iterations allowed fast model execution to work out the approach.  This yielded a result slightly better than a guess with 61% accuracy.

I then set-up a transfer model with a VGG16 base model and similar layers.  This reduced the accuracy to 58%.  More data is needed.

The challenge going forward will be to adjust the parameters to improve the accuracy while managing the execution time to complete by the due date.  I will start by setting up a simple logistic regression model as the baseline. Then assess the different baseline models to see which is best for the low-level classification. Finally, I will work on the fine-grained classification.
