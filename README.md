DNet Project
============

### QUESTION 1:

The first part of the task was to analyze two `.csv` files and write some codes to process them. The current directory
contains the required codes to answer those questions.

#### Structure of the code:
This task was written both as a regular OOP Python and as a Jupyter Notebook. These files are contained in the `src`
directory in the project. The `resources` directory contains the `.csv` files required for the project. 

##### Note: this project was implemented using only Pandas, version 0.25.3. Since Pandas is a very active library with lots of updates frequently, using a different version might cause some warnings or `deprecation` errors. To ensure using the same Pandas version please run the followin:

`pip install -r requirements.txt`

The `main.py` code can be run by simply running the entire file in a Python environment. Example, run the following
command in a terminal shell:

`$>> python main.py`

The above command would print the results on the shell. For question c, it would also save the new `opioids.csv` file in
`resources` directory.

### QUESTION 2:
a) <em>Suppose we collect new drug listings as in ‘Listings.csv’, this time without a ‘Level 1’ label. If we assume all
 listings belonging to each ‘Level 1’ class are similar in some way and we want to use a Machine Learning model to 
 predict that class, name and briefly describe how such a model could be implemented?</em>
 
This is a supervised, multi-label classification problem. For such a task, one would first need construct the training
set with the <strong>X</strong> data matrix as the drug listing and the <strong>y</strong> data vector as our ground-truth labels. The ground truth
labels must first be converted into some sort of binary form (e.g. using one-hot encoding). Since the <strong>X</strong> matrix 
contains texts, it must also be vectorized to be prepared for the model training. There a number of different 
approaches that could be used, for example Bag-of-Words. This algorithm can be used through for example the 
Scikit-learn’s `CountVectorizer` method.

For building the predictive model, there are different options for the classification algorithm. Since creating a
model is now quite simple and straightforward using standard Python packages (e.g. Scikit-learn, TensorFlow etc.), 
we could even benchmark a number of them and select the one with the best performance. 

Examples of a predictive model for DNet task:
-	Naïve Bays approach, 
-	Support vector machines, 
-	Logistic regression, 
-	Random forest,
-	etc.

There are many things to consider when implementing this model. One of the main issues that we might face would be 
class imbalance. Another issue could be not enough data. There are ways to account for theses issues too: 
for example using techniques such as SMOTE (a resampling technique) to correct the class imbalance, 
and data augmentation for generating more data.

b) <em> Suppose we implemented a machine learning model to predict the ‘Level 1’ class, describe one method to 
validate the accuracy of our model.</em>

b)	Suppose we implemented a machine learning model to predict the ‘Level 1’ class, describe one method to validate 
the accuracy of our model.