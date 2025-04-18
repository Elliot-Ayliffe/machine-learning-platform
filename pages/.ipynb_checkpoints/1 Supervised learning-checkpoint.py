import streamlit as st
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,classification_report,accuracy_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.datasets import make_classification,make_blobs
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder


from Modules.supervised_functions import subpage1, subpage2, subpage3, subpage4, supervised_quiz


st.title("Supervised Learning ")

tab1, tab2, tab3, tab4 = st.tabs(['Introduction', 'Different models', 'Car Accident Prediction', 'Film Rating Prediction'])


with tab1:

    st.write("🎉🎉🎉If you've made it this far, it means you're genuinely interested in this topic, and the content ahead is definitely worth looking forward to!🎉🎉🎉")

    st.header("What is Supervised Learning ")
    st.write("Supervised learning is one of the core techniques in machine learning. Think of it like teaching a model with examples: you provide it with data (the inputs) along with the correct answers (the outputs), and it learns to make predictions based on that. These predictions can be continuous values (like predicting house prices—this is called regression) or categories (like identifying if an email is spam or not—this is called classification).")
    st.write("After being trained on labeled examples, the model can then make educated guesses on new, unseen data. This ability to generalize is key, and it mirrors how humans learn to recognize patterns and form concepts.")
    st.write("(*Based on [Wikipedia](https://en.wikipedia.org/wiki/Supervised_learning)*)")

    st.header("Supervised Learning in the ***:rainbow[real-world]***")
    st.write("Due to its powerful predictive capabilities and broad applicability, supervised learning has a wide range of applications in many fields. Here are some of the main application areas:")
    
    st.subheader("Image Recognition")
    st.write("Facial Recognition: Used in security systems and social media (e.g., for automatic photo tagging).")
    st.write("Object Detection: Detecting pedestrians and vehicles in autonomous driving, and abnormal behaviors in security surveillance.")
    st.write("Medical Imaging Analysis: Used for disease diagnosis (e.g., cancer detection, X-ray image analysis).")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/1_supervised_images/Facial Recognition.jpg", caption="Facial Recognition", use_container_width=True)

    st.subheader("Natural Language Processing (NLP)")
    st.write("Sentiment Analysis: Analyzing the sentiment (positive, negative, or neutral) in text (e.g., social media posts, product reviews).")
    st.write("Machine Translation: Translating text from one language to another.")
    st.write("Converting speech signals into text (e.g., in smart voice assistants)")
    st.write("Text Classification: Categorizing text into different classes (e.g., news classification, spam detection).")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/1_supervised_images/ORC.png", caption="ORC", use_container_width=True)

    st.subheader("Gaming and Entertainment")
    st.write("Game Recommendation: Recommending games based on players' gaming history and preferences.")
    st.write("In-Game Character Behavior Prediction: Predicting character behavior based on player data to optimize the gaming experience.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/1_supervised_images/OIP.jpg", caption="OIP", use_container_width=True)

    
    st.write("Of course, there are many other application scenarios. Supervised learning is widely applied and deeply integrated into various aspects of daily life, making it an accessible and practical tool.")

with tab2:
    st.header("Which Supervised Learning model would you like?")
    st.write("No matter where it is applied, the underlying logic is consistent. Starting from the basics is a necessary path to becoming a master. Choose a direction that interests you and dive in. :diving_mask: ")

    summaries = {
        "Linear Regression": "Linear regression is one of the most fundamental supervised learning algorithms, primarily used for predicting continuous target variables. It assumes a linear relationship between input features and the target variable and attempts to find the best-fitting line to describe this relationship.",
        "Logistic Regression": "Logistic regression is mainly used for binary classification problems. It maps the results of linear regression to values between 0 and 1 using a logistic function, thereby predicting the probability of an event occurring.",
        "Support Vector Machine": "Support Vector Machine (SVM) is a powerful classification algorithm that maximizes the margin between different classes by finding an optimal decision boundary. SVM can also be used for regression problems.",
        "Random Forest": "Random Forest is an ensemble learning method that improves the generalization ability of the model by constructing multiple decision trees and averaging or voting on their results."
    }
    selected_method = st.selectbox(
        "Pick a model!",
        options=list(summaries.keys())
    )

    if selected_method == "Linear Regression":
        subpage1(summaries[selected_method])
    elif selected_method == "Logistic Regression":
        subpage2(summaries[selected_method])
    elif selected_method == "Support Vector Machine":
        subpage3(summaries[selected_method])
    elif selected_method == "Random Forest":
        subpage4(summaries[selected_method])

    st.divider()

    st.subheader("Quiz time!")
    st.write("How much have you learnt?!?")

    supervised_quiz()

with tab3:
    
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Here , we created a model using **real data** which can be used to classify the severity of some car crashes. used random forest. give a bit more background etc etc")
    
    with col2:
        st.image('images/1_supervised_images/cars_onroad.jpg')
    
    # Load Dataset
    @st.cache_data
    def clean_data(df):
        
        # st.dataframe(df.head())

        df['SPEEDING'] = df['SPEEDING'].fillna('N')
        df['SPEEDING'] = df['SPEEDING'].replace(r'^\s*$', 'N', regex=True)

        df['SPEEDING'] = df['SPEEDING'].map({'Y': 1, 'N': 0})
        df = df.dropna()  # Drop missing values

        df['SEVERITYCODE'] = df['SEVERITYCODE'].map({'0': 0, '1':1, '2':2, '2b':3, '3':4})  
        
        # List of categorical features
        categorical_features = ['WEATHER', 'ROADCOND', 'LIGHTCOND']

        # Convert categorical features to numerical labels
        encoder = OrdinalEncoder()
        df[categorical_features] = encoder.fit_transform(df[categorical_features])
        return df

    data = pd.read_csv('datasets/Collisions.csv')
    
    # Sample Features
    df = data[['SEVERITYCODE', 'WEATHER', 'ROADCOND', 'LIGHTCOND', 'SPEEDING']] # +junctiontype/ addrtype

    st.write("This is the data we're using:")
    st.dataframe(df.head())
    
    st.write("Some of the columns are categories. This does not work well in (something - rf clas?) because (reason). therefore we need to change them to numerical values")
    st.write("There are also missing vlaues which need to be cleaned. [Explain how they were cleaned]")
    
    # Load data
    df = clean_data(df)
    
    st.dataframe(df.head())


    df.fillna('0', inplace=True) 

    X = df.drop(columns=['SEVERITYCODE'])
    y = df['SEVERITYCODE']

    st.header('Predicting Accident Severity - Random Forest Classifier')

    st.write("Lets have a look at the distribution of crash severity values")

    # Visualize Class Distribution of Severity Code
    st.subheader(" Distribution of Accident Severity")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(x=df['SEVERITYCODE'], palette='viridis', ax=ax)
    ax.set_xlabel("Severity Code")
    ax.set_ylabel("Count")
    # ax.set_yscale('log')
    st.pyplot(fig)

    st.write('The plot above shows the severity distribution of car accidents in Seattle. 0 = Unknown, 1 = Prop damage, 2 = Minor injury, 3 = Serious injury, 4 = Fatality. What factors could we use to predict the outcome for a given accident?')

    st.write("We can clearly see that the majority of crashes have severity of 1 or 2. Very low or very high severity crashes are rare. ")

    # st.write("Dataset Preview:", df.head())  # Show first 5 rows

    

    # Streamlit Sidebar for Feature Selection
    st.header("Select Features for Prediction")
    
    st.write("GIVE OVERVIEW OF WHATS HAPPENING HERE. ")
    st.write("go step by step through what you're doing, why you're doing it, and what it shows. ")
    
    
    selected_features = st.multiselect("Choose features to include", X.columns.tolist(), default=X.columns.tolist())

    # Train Model on Selected Features
    if selected_features:
        if X[selected_features].shape[0] == 0:
            st.error("No data available after filtering. Try selecting different features.")
            st.stop()

        # Sliders for Model Parameters (Main Layout)
        st.header("🔧 Adjust Model Parameters")

        col1, col2, col3 = st.columns(3)

        with col1:
            n_estimators = st.slider("Number of Trees", min_value=10, max_value=500, value=100, step=10)

        with col2:
            max_depth = st.slider("Max Depth", min_value=1, max_value=50, value=10, step=1)

        with col3:
            min_samples_split = st.slider("Min Samples Split", min_value=2, max_value=20, value=2, step=1)        
    
        X_train, X_test, y_train, y_test = train_test_split(X[selected_features], y, test_size=0.2, random_state=1)
        
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)
        model.fit(X_train, y_train)

        st.write("Feature Importances:", model.feature_importances_)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Display Performance Metrics
        st.write("## Model Performance")
        
        st.write("EXPLAIN WHAT THIS MEANS AND WHAT IT SHOWS")
        st.write(f"**Model Accuracy with Selected Features:** {accuracy:.4f}")
        
        feature_importances = pd.DataFrame({
            'Feature': selected_features,
            'Importance': model.feature_importances_
        })

        if feature_importances["Importance"].sum() == 0:
            st.error("All feature importances are zero. Try selecting different features or check dataset preprocessing.")
            st.stop()

        # Feature Importance Visualization
        st.write("**Feature Importance**")
        feature_importances = pd.DataFrame({'Feature': selected_features, 'Importance': model.feature_importances_}).sort_values(by="Importance", ascending=False)

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x="Importance", y="Feature", data=feature_importances, ax=ax)
        ax.set_title("Feature Importance")
        st.pyplot(fig)
    else:
        st.warning("Please select at least one feature to train the model.")

    st.write("Explain what this shows.")
    
    st.write("Also reiterate what they've learnt/ why this is useful. ")


with tab4:
    @st.cache_data
    def load_imdb_data():
        df = pd.read_csv('datasets/IMDb_Dataset.csv')  # Update path
        df = df[['IMDb Rating', 'Genre', 'Duration (minutes)', 'Year']]  # Sample Features

        # Handle Missing Values
        df = df.dropna()

        # Encode Categorical Features
        categorical_features = ['Genre']
        encoder = OrdinalEncoder()
        df[categorical_features] = encoder.fit_transform(df[categorical_features])

        return df

    # Load IMDb data
    df_imdb = load_imdb_data()

    # Split Features and Target
    X_imdb = df_imdb.drop(columns=['IMDb Rating'])
    y_imdb = df_imdb['IMDb Rating']

    # Streamlit UI
    st.header("Predicting IMDb Film Ratings with Linear Regression")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("intro to the page, what are you doingn here, what tool are you using, and why.")
    with col2:
        st.image('images/1_supervised_images/imdb.png')

    st.write('As we are predicting a continuous variable (rating /10), here we use a **regression** approach instead of classification. EXPLAIN WHY THERES A DIFFERENCE?')
    st.write('Dataset Preview:', df_imdb.head())

    # Feature Selection
    st.subheader("Select Features for Prediction")
    selected_features_imdb = st.multiselect("Choose features", X_imdb.columns.tolist(), default=X_imdb.columns.tolist())

    # Train Model if Features Are Selected
    if selected_features_imdb:
        X_train, X_test, y_train, y_test = train_test_split(X_imdb[selected_features_imdb], y_imdb, test_size=0.2, random_state=42)

        # Train Linear Regression Model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predictions
        y_pred = model.predict(X_test)

        # Performance Metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        st.write("## Model Performance")
        st.write(f"**Mean Absolute Error (MAE):** {mae:.4f}")
        st.write(f"**Mean Squared Error (MSE):** {mse:.4f}")
        st.write(f"**R² Score:** {r2:.4f}")

        # Coefficients (Feature Importance in Linear Regression)
        coefficients = pd.DataFrame({
            'Feature': selected_features_imdb,
            'Coefficient': model.coef_
        }).sort_values(by="Coefficient", key=abs, ascending=False)  # Sort by absolute value

        st.write("**Feature Coefficients**")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x="Coefficient", y="Feature", data=coefficients, ax=ax)
        ax.set_title("Feature Coefficients")
        st.pyplot(fig)
        
        st.write("Explain here what this shows eg longer/older films => better rated")

    else:
        st.warning("Please select at least one feature to train the model.")

    # Quiz: Least Important Feature (Smallest Absolute Coefficient)
    st.header("🧠 Quiz: Identify the Least Important Feature!")

    if not coefficients.empty:
        # Get the feature with the smallest absolute coefficient
        least_important_feature = coefficients.iloc[-1]['Feature']

        # Quiz options (fixed order)
        quiz_options = coefficients['Feature'].tolist()

        # Ask the question
        selected_answer = st.radio(
            "Which feature has the **least** impact (smallest absolute coefficient) in the model?",
            quiz_options, index=None
        )

        # Check if the answer is correct
        if st.button("Submit Answer 2"):
            if selected_answer == least_important_feature:
                st.success(f"✅ Correct! The least important feature is **{least_important_feature}**.")
            # leave blank if no answer selected
            elif selected_answer==None:
                st.write("")
            else:
                st.error(f"❌ Incorrect. The least important feature is **{least_important_feature}**.")    