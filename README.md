# TweetBot

## Introduction

This is a basic command line application that allows the user to post a quick tweet on Twitter if they want to while using the command line. This uses webscraping to manage the html points within the Twitter pages.

## Live Demo URL

https://drive.google.com/file/d/1dtcWgyMfEgKAyvmZm6_N2Hb7TsdMeMBx/view

## GitHub Repo

https://github.com/TheBigBookMan/TweetBot

## Initialization

In root folder

```
python main.py
```

## Functionality

This application uses Python and the Selenium and WebDriver packages to allow for webscraping. The command line interface will ask the user for their Twitter username, password and what they want to tweet about. Using selenium and the webdriver allows the application to find the correct path through the HTML of the Twitter pages and signs the user in, then creates a tweet, uploads it and then goes to the users profile to view the posted tweet.

![](/TweetBot.png)
