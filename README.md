# Video Game Recommender

This project is a video game recommendation system based on k nearest neighbor content based filtering. The goal of this application is to provide the user with useful gaming recommendation based on their preferences entered in web hosted user interface.
<br>
Check out our App here [Video Game Recommender](https://vgame-recommender.herokuapp.com/)

## Workflow
### 1. Preprocessing
* Our [data set](https://www.kaggle.com/ashaheedq/video-games-sales-2019?select=vgsales-12-4-2019.csv) is from kaggle. The initial source had over 55,000 records of video game sales/scores up until 2019.
* This was read into a Jupyter notebook for preprocessing and data cleanup where columns with irrelevant data or null values were removed
* We also prepared our data for machine learning application by transforming categorical data to numerical for testing using the get dummies function

### 2. Machine Learning & Model
* We implemented the k-nearest neighbors model algorithm for our recommender.
<img width="243" alt="filtering" src="https://user-images.githubusercontent.com/85762953/145692582-93f31883-a716-4d9f-b3c1-6f2fea9c74d5.png">

### 3. Cloud Deployment 
* Web app deployed using flask and via the cloud with Heroku 

### 4. Limitations  
* We lost more than 90% of our original data due to so many columns having null values. 
* Time constraint: If we had more time we would implement more filters and search features for the users to get an even more accurate recommendation. We also would have added live data to the home page under the videogame statistics counter.


## References


<details>
<summary> Tools, Languages, & Libraries Utilized</summary>
<li>Python</li></ul>
<li>Pandas</li></ul>
<li>Tensorflow</li></ul>
<li>Flask</li></ul>
<li>Numpy</li></ul>
<li>NearestNeighbors</li></ul>
<li>sklearn</li></ul>
<li>Jupyter Notebook</li></ul>
<li>VS Code</li></ul>
<li>Jupyter Notebook</li></ul>
<li>HTML</li></ul>
<li>CSS</li></ul>
<li>deployed via Heroku</li></ul>

</details>

<details>
<summary>Game Statistics (Links) </summary>
<li>https://www.githyp.com/</li></ul>
<li>https://variety.com/2021/gaming/news/number-video-game-players-2021-esa-study-covid-1235016079/</li></ul>
<li>https://www.ign.com/articles/best-selling-video-game-consoles</li></ul>
</details>

# 

### Collaborators
|[Dillon](https://github.com/rb25s13)|[Felecia](https://github.com/fhelms8)|[Matthew](https://github.com/Mvillarreal88)|[Michelle](https://github.com/michelleherman13)|
|---|---|---|---|
