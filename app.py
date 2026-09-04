from flask import Flask,render_template,request
import json
import requests

app = Flask(__name__)

@app.route('/world')
def world():
    response_world = requests.get('https://newsapi.org/v2/everything?q=world&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_world.status_code == 200:
        data_world = response_world.json()
        artical_world = data_world['articles']
        world ={}
        for i in range(0,len(artical_world)):
            titles = data_world['articles'][i]['title']
            disc = data_world['articles'][i]['description']
            img = data_world['articles'][i]['urlToImage']
            time_publish = data_world['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_world['articles'][i]['content']
            link = data_world['articles'][i]['url']
            world[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                    }
        l=len(world)
        return render_template("worlds.html",world=world,l=l)


@app.route('/politics')
def politics():
    response_politics = requests.get('https://newsapi.org/v2/everything?q=indian politics&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_politics.status_code == 200:
        data_politics = response_politics.json()
        artical_politics = data_politics['articles']
        politics ={}
        for i in range(0,len(artical_politics)):
            titles = data_politics['articles'][i]['title']
            disc = data_politics['articles'][i]['description']
            img = data_politics['articles'][i]['urlToImage']
            time_publish = data_politics['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_politics['articles'][i]['content']
            link = data_politics['articles'][i]['url']
            politics[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                    }
        l=len(politics)
        return render_template("politics.html",politics=politics,l=l)


@app.route('/sports')
def sports():
    response_sports = requests.get('https://newsapi.org/v2/everything?q=indian sports&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_sports.status_code == 200:
        data_sports = response_sports.json()
        artical_sports = data_sports['articles']
        sports ={}
        for i in range(0,len(artical_sports)):
            titles = data_sports['articles'][i]['title']
            disc = data_sports['articles'][i]['description']
            img = data_sports['articles'][i]['urlToImage']
            time_publish = data_sports['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_sports['articles'][i]['content']
            link = data_sports['articles'][i]['url']
            sports[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                    }
        l=len(sports)
        return render_template("sports.html",sports=sports,l=l)


@app.route('/entertainment')
def entertainment():
    response_entertainment = requests.get('https://newsapi.org/v2/everything?q=entertainment india&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_entertainment.status_code == 200:
        data_entertainment = response_entertainment.json()
        artical_entertainment = data_entertainment['articles']
        entertainment ={}
        for i in range(0,len(artical_entertainment)):
            titles = data_entertainment['articles'][i]['title']
            disc = data_entertainment['articles'][i]['description']
            img = data_entertainment['articles'][i]['urlToImage']
            time_publish = data_entertainment['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_entertainment['articles'][i]['content']
            link = data_entertainment['articles'][i]['url']
            entertainment[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                    }
        l=len(entertainment)
        return render_template("entertainment.html",entertainment=entertainment,l=l)


@app.route('/technology')
def technology():
    response_technology = requests.get('https://newsapi.org/v2/everything?q=india technology&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_technology.status_code == 200:
        data_technology = response_technology.json()
        artical_technology = data_technology['articles']
        technology ={}
        for i in range(0,len(artical_technology)):
            titles = data_technology['articles'][i]['title']
            disc = data_technology['articles'][i]['description']
            img = data_technology['articles'][i]['urlToImage']
            time_publish = data_technology['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_technology['articles'][i]['content']
            link = data_technology['articles'][i]['url']
            technology[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                    }
        l=len(technology)
        return render_template("technology.html",technology=technology,l=l)

    

@app.route("/searchresult",methods=['GET','POST'])
def searchresult():
    r = None
    if request.method=='POST':
         r = request.form.get('search')
    
    response_search = requests.get(f'https://newsapi.org/v2/everything?q={r}&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response_search.status_code == 200:
        data_search = response_search.json()
        artical_search = data_search['articles']
        search ={}
        for i in range(0,len(artical_search)):
            titles = data_search['articles'][i]['title']
            disc = data_search['articles'][i]['description']
            img = data_search['articles'][i]['urlToImage']
            time_publish = data_search['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data_search['articles'][i]['content']
            link = data_search['articles'][i]['url']
            search[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
                }
        l=len(search)
        return render_template("search_result.html",search=search,l=l)
            

    



@app.route("/",methods=['GET','POST'])
def home():
    r = "rajasthan"
    if request.method=='POST':
        r = request.form.get('weather_search')
    api_key = '83820186ae2de37f7adcf99c24068128'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={r}&appid={api_key}&units=metric'
    data = requests.get(url)
    weather = {}
    if data.status_code == 200:
        info = data.json()
        weather={
            "city" :info['name'],
            "temprature":info['main']['temp'],
            "minimum_temprature":info['main']['temp_min'],
            "feels_like":info['main']['feels_like'],
            "humidity":info['main']['humidity'],
            "pressure":info['main']['pressure'],
            "wind_speed":info['wind']['speed'],
            "sky":info['weather'][0]['main']
            }
    else:
        print('City is incorrect')
    

    response = requests.get('https://newsapi.org/v2/everything?q=sports in india&apiKey=9d2377590e0b4948a896e81a370146e0')
    if response.status_code == 200:
        data = response.json()
        artical = data['articles']
        final ={}
        for i in range(0,len(artical)):
            titles = data['articles'][i]['title']
            disc = data['articles'][i]['description']
            img = data['articles'][i]['urlToImage']
            time_publish = data['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = data['articles'][i]['content']
            link = data['articles'][i]['url']
            final[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
            }

    
    responseh = requests.get('https://newsapi.org/v2/everything?q=india&apiKey=9d2377590e0b4948a896e81a370146e0')
    if responseh.status_code == 200:
        datah = responseh.json()
        articalh = datah['articles']
        headlines ={}
        for i in range(0,len(articalh)):
            titles = datah['articles'][i]['title']
            disc = datah['articles'][i]['description']
            img = datah['articles'][i]['urlToImage']
            time_publish = datah['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = datah['articles'][i]['content']
            link = datah['articles'][i]['url']
            headlines[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
            }


    responset = requests.get('https://newsapi.org/v2/everything?q=Technology&apiKey=9d2377590e0b4948a896e81a370146e0')
    if responset.status_code == 200:
        datat = responset.json()
        articalt = datat['articles']
        tech ={}
        for i in range(0,len(articalt)):
            titles = datat['articles'][i]['title']
            disc = datat['articles'][i]['description']
            img = datat['articles'][i]['urlToImage']
            time_publish = datat['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = datat['articles'][i]['content']
            link = datat['articles'][i]['url']
            tech[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
            }


    responsee = requests.get('https://newsapi.org/v2/everything?q=Entertainment in india&apiKey=9d2377590e0b4948a896e81a370146e0')
    if responsee.status_code == 200:
        datae = responsee.json()
        articale = datae['articles']
        entertain ={}
        for i in range(0,len(articale)):
            titles = datae['articles'][i]['title']
            disc = datae['articles'][i]['description']
            img = datae['articles'][i]['urlToImage']
            time_publish = datae['articles'][i]['publishedAt']
            date = time_publish[0:10]
            time = time_publish[12:19]
            con = datae['articles'][i]['content']
            link = datae['articles'][i]['url']
            entertain[i]={
                'titles' : titles,
                'disc':disc,
                'img':img,
                'date':date,
                'time':time,
                'con':con,
                'link':link
            }    

        


        return render_template("index.html",headlines=headlines,final=final,tech=tech,entertain=entertain,weather=weather)


if __name__=="__main__":
    app.run(debug=True,port=5000,host='localhost')


