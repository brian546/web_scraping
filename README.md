# Analyze Popularity of Japanese Restaurant in Hong Kong Island

The project aims to collect data from OpenRice using web scrapping and analyze the the best strategy for running a Janpanese restaurant in Hong Kong Island

## Data Collection
We have collected restaurant id, address, number of bookmarks, price range, likes, dislikes, type of cuisine, and number of reviews.
<br/>
<br/>
<img height="400" alt="image" src="https://user-images.githubusercontent.com/43593664/117918525-c7a78480-b31d-11eb-91bf-a0d5c001129c.png">

## Data Preprocessing

### Filter out district from address
To grouping the restaurants into same districts, we filtered out the district, which is after the last ',' of address.
<br/>
<br/>
<img width="407" alt="image" src="https://user-images.githubusercontent.com/43593664/117918827-6fbd4d80-b31e-11eb-8390-9a8c425e99b8.png">

### Grouping fusion cuisine together
As some types of cuisine of the Japanese Restaurant are Shanghai, Taiwan, Brazilian, French, etc., we map them all into 'fusion' 
<br/>
<br/>
<img width="587" alt="image" src="https://user-images.githubusercontent.com/43593664/117919385-78625380-b31f-11eb-9b16-68de2281e35e.png">

## Theory
To evaluate the profitability of these Japanese restaurants, we made the following assumsions and compare the popularity between groups in aspects of location(district), type of cuisine, and price range.
<br/>
<img style="display: inline-block;" width="400px" alt="image" src="https://user-images.githubusercontent.com/43593664/117919583-dd1dae00-b31f-11eb-9ccd-5d126842c2db.png">
<br/>
<img style="display: inline-block;" width="400px" alt="image" src="https://user-images.githubusercontent.com/43593664/117919605-e3ac2580-b31f-11eb-823e-946d9be2bf8d.png">


## Result

### Location 
The top 5 mean populairity of location at where Japanese restaurant is opened are Causeway Bay, Central, Sheung Wan, Wan Chai, and Repulse Bay. 
![image](https://user-images.githubusercontent.com/43593664/117920092-d93e5b80-b320-11eb-8d96-4f5ad5199ae4.png)

### Price Range
The result showed that the retaurants with higher price range tends to be more popular. 
![image](https://user-images.githubusercontent.com/43593664/117920482-81ecbb00-b321-11eb-8834-fe8c4276e3ee.png)
<br/>

### Cuisine
All-you-can-eat and buffet are the 2 most popular type of Japanese cuisine 
<img width="610" alt="image" src="https://user-images.githubusercontent.com/43593664/117920814-2969ed80-b322-11eb-9c3b-775496ebac84.png">

## Conclusion
<img width="700" alt="image" src="https://user-images.githubusercontent.com/43593664/117920887-55856e80-b322-11eb-9b2a-30002d73f76f.png">





