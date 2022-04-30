# Safe Hotel Booking System

### Environment set up

Strongly recommend to run on an [anaconda](https://www.anaconda.com/) environment! 

*Python package (based on Anaconda Virtual Environment):*

Flask : `pip install Flask`

requests : `python -m pip install requests`

pandas : `conda install pandas`

matplotlib : `conda install matplotlib`

First clone this project and ***cd*** to ***flaskr*** folder, install the necessary packages above, run this project based on your terminal type, for Bash the command is shown below, for other types please check [flask env setup](https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/):

```shell
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

then you will see output similar to the image below, click the URL link to explore:

![img](https://s2.loli.net/2022/04/30/oi9YCd5z6uSkmRa.png)

### Data Source

This website using this four APIs

[*Booking.com API*](https://rapidapi.com/tipsters/api/booking-com/) 

[*Google Map API*](https://developers.google.com/maps) 

[*Crime Data in Chicago*](https://data.cityofchicago.org/Public-Safety/Crimes-One-year-prior-to-present/x2n5-8w5q/data)

[*Police Stations in Chicago*](https://data.cityofchicago.org/Public-Safety/Police-Stations/z8bn-74gv) 

Pay attention to the Booking.com API and Google Map API should use your personal API key! 

### Website Overview

![image-20220429200458142](https://s2.loli.net/2022/04/30/j8oIunBJPbmihYk.png)

![image-20220429200514505](https://s2.loli.net/2022/04/30/P1IHUeEhWt27kZM.png)

![](https://s2.loli.net/2022/04/30/BtlVXmINqvuo5pJ.png)

![image-20220429200544346](https://s2.loli.net/2022/04/30/kEMaPCgi1Qqc7Ij.png)