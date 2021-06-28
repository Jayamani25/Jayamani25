{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOXA6uZnHC2RSPijZBwHJkE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Jayamani25/Jayamani25/blob/main/Weather%20Report.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_iNxXOPboFoM",
        "outputId": "c5f85242-2385-4776-c5a1-cb8fc5489440"
      },
      "source": [
        "import requests\n",
        "from datetime import datetime\n",
        "date_time=datetime.now()\n",
        "print(\"Date and Time==\",date_time)\n",
        "location=input(\"Enter the city:\")\n",
        "api_link='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=1d186ff9cd5f36400f7ead29dc4f328c'\n",
        "print(\"Name Of The city==\",location.upper())\n",
        "link=requests.get(api_link)\n",
        "data=link.json()\n",
        "temp_city=((data['main']['temp'])-273.15)\n",
        "tempmin_city=((data['main']['temp_min'])-273.15)\n",
        "tempmax_city=((data['main']['temp_max'])-273.15)\n",
        "humidity_city=(data['main']['humidity'])\n",
        "wind_city=(data['wind']['speed'])\n",
        "lat_city=(data['coord']['lat'])\n",
        "lon_city=(data['coord']['lon'])\n",
        "\n",
        "print(\"---------------------------------------------------------------\")\n",
        "print(\"Temperature Of The City        ==\",temp_city)\n",
        "print(\"Minimum Temperature Of The city==\",tempmin_city)\n",
        "print(\"Maximum Temperature Of The City==\",tempmax_city)\n",
        "print(\"Humidity Of The city           ==\",humidity_city)\n",
        "print(\"Wind Speed Of The City         ==\",wind_city)\n",
        "print(\"Latitude Of The City           ==\",lat_city)\n",
        "print(\"Longitude Of The City          ==\",lon_city)\n",
        "print(\"---------------------------------------------------------------\")\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Date and Time== 2021-06-28 10:13:26.616358\n",
            "Enter the city:chennai\n",
            "Name Of The city== CHENNAI\n",
            "---------------------------------------------------------------\n",
            "Temperature Of The City        == 31.090000000000032\n",
            "Minimum Temperature Of The city== 31.090000000000032\n",
            "Maximum Temperature Of The City== 34.99000000000001\n",
            "Humidity Of The city           == 79\n",
            "Wind Speed Of The City         == 2.24\n",
            "Latitude Of The City           == 13.0878\n",
            "Longitude Of The City          == 80.2785\n",
            "---------------------------------------------------------------\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}