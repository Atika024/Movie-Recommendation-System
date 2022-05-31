# Movie-Recommendation-System
A content based movie recommender system using cosine similarity

-**Dataset link:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
-**Programming language:** Python
-**API:** TMDB
-**Framework:** Streamlit
-**Libraries:** Pandas, NumPy
-**IDE used:** Jupyter Notebook and Pycharm

**How to get the API key?**
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

**How to run the project?**
1. Clone or download this repository to your local machine.
2. Download the dataset
3. Run the jupyter notbook code to get required dataframes.
4. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
5. Get your API key from https://www.themoviedb.org/. 
6. Replace YOUR_API_KEY in both the places (line no. 15 and 29) of static/recommend.js file and hit save.
7. Open your terminal/command prompt from your project directory and run the file app.py by executing the command streamlit run app.py
8. This will redirect you to your local browser where you can check the working of the web app.
