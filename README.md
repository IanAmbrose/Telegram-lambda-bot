<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/IanAmbrose/telegram-lambda-bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Telegram Bot</h3>
  <h4 align="center">AWS (Lambda & API Gateway)</h4>

  <p align="center">
    <br />
    <i>In this guide I will demonstrate making a simple serverless Telegram bot that echoes everything <br />
      a user inputs and replies with the message reversed, using AWS API Gateway and AWS Lambda.</i>
    <br />
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#setup-guide">Getting Started</a>
      <ul>
        <li><a href="#telegram-bot-setup">Telegram Bot Setup</a></li>
        <li><a href="#creating-an-api-gateway">Creating an API Gateway</a></li>
        <li><a href="#connecting-lambda-function-to-api-gateway">Connecting Lambda function to API Gateway</a></li>
        <li><a href="#setting-webhooks">Setting Webhooks</a></li>
        <li><a href="#adding-code-to-lambda-function"><li><a href="#setting-webhooks">Adding Code to Lambda Function</a></li></a></li>
        <li><a href="#testing"><li><a href="#setting-webhooks">Testing</a></li></a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Detailed instructions on how to setup a telegram bot and provide integration with Amazon Web Service (AWS) serverless functions.
Functionally this project takes any message sent to the telegram bot and replies with the reverse of the message.

### Built With
* [Python](https://www.python.org/)
* [AWS Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1#/discover)
* [AWS API Gateway](https://console.aws.amazon.com/apigateway/main/apis?region=us-east-1)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Setup Guide

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Telegram Bot Setup

To continue with this guide, you will need to have a telegram bot setup
1. Open a new message on telegram with the user "BotFather"
2. Message BotFather with "/newbot"
3. Take note of the HTTP API key:
   
![API](https://user-images.githubusercontent.com/74079455/152599353-def39406-fc00-4b52-8f37-8d4a80a17133.png)
<br></br>

### Creating an API Gateway 

Before being able to create an API Gateway An Amazon Web Services account is required a free tier can be created at  <a href="https://aws.amazon.com/">AWS Console</a> 

1. Once singed into AWS (Amazon Web Service), Search for <b> API GATEWAY</b>
2. Select REST API
3. Select New API, Enter a API Name & Description and select Create API
  
![new-API-ConvertImage](https://user-images.githubusercontent.com/74079455/152593667-eadb0a16-7ef1-4509-9ecd-94206dd74fc9.png)
  
<p align="right">(<a href="#top">back to top</a>)</p>


### Creating a lambda function

Return to <a href="https://aws.amazon.com/">AWS Console</a> and search for and select Lambda Service

1. Select "Create Function"
2. Choose 'Author from scratch'
3. Enter Basic Information - Function Name and Language, for this guide select Python 3.6
4. Choose 'Change default execution role' from the Permissions header 
5. Next apply the setting found in the screenshot below:

![role---Copy-ConvertImage](https://user-images.githubusercontent.com/74079455/152596274-40f01010-8c36-4ff6-b672-face9f5aa216.png)
  

<p align="right">(<a href="#top">back to top</a>)</p>


### Connecting Lambda function to API Gateway

Return to <a href="https://aws.amazon.com/">AWS Console</a> and search for and select <b>API Gateway</b> From the services

1. Select the API previously created
2. Select the "Actions" drop down menu, and select <b>"Create Method"</b>
3. From there you will see a <b>"/"</b>, click this and select <b>"ANY"</b>
4. Now hit the check sign next to <b>"ANY"</b>
5. From Here choose <b>"Lambda Function"<b> for the intergration type and select <b>"Use Lambda Proxy Integration"<b>
6. Then insert a Lambda Function name and <b>click save</b>
7. Then from the "Actions" Drop down select <b>"Deploy API"</b>
8. Select <b>"New Stage"</b> and select a stage name e.g<b>"Beta"</b>
9. Once your API is deployed you will get a <b>"Invoke URL"</b> - <i>(click the link and it should display "Hello from Lambda!")</i>
  10. Store the <b>"Invoke URL"</b> as its needed for setting up webhooks
  

![role---Copy-ConvertImage](https://user-images.githubusercontent.com/74079455/152596274-40f01010-8c36-4ff6-b672-face9f5aa216.png)
  

<p align="right">(<a href="#top">back to top</a>)</p>
  
### Setting Webhooks
  
  Now we have the URL setup in the previous stage, we now need to tell telegram to send all future messages to that address<br  />
  
 Copy, edit and paste the URL below into your web brower:<br  />
  
  `https://api.telegram.org/bot(your-bot-token)/setWebHook?url=(your-API-invoke-URL)`
  
  <i>Note:</i><br  />
  <i> Replace (your-bot-token) with the API Token stored in  <a href="#telegram-bot-setup">Telegram Bot setup</a><br  /></i>
  <i> Replace (your-API-invoke-URL) with the invoke URL stored from  <a href="#connecting-lambda-function-to-api-gateway">Connecting Lambda function to API Gateway</a></i>
<br  />
<br  />
     
  
### Adding code to Lambda function

Return to <a href="https://aws.amazon.com/">AWS Console</a> and search for and select <b>Lambda</b> From the services

1. Select the Lambda <b>"Functions"</b> tab
2. Select the function perviously made
3. Scroll down to Code source
4. Replace all code and Insert the reverse message code below, remembering to replace (your-bot-token) with the API code stored from <a href="#telegram-bot-setup">Telegram Bot setup</a><br  />
```Python
    
import json
from botocore.vendored import requests

TELE_TOKEN='(your-bot-token)'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)


def send_message(text, chat_id):
    final_text =  reverse(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
    requests.get(url)
    
def reverse(string):
    string = string[::-1]
    return string
    
def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']
    send_message(reply, chat_id)
    
    return {
        'statusCode': 200
    }
``` 
<br  />
    
   ### Testing
    
   
  Return to Telegram and open messages with <b>"BotFather"</b> and now click the link at the top of the "Congratulations" message.
  This will take you to your bot,<br  />
  Now test your bot now works by messaging your bot on telegram.<br  />
  
![image](https://user-images.githubusercontent.com/74079455/152615748-699e712b-007b-41a5-b8ec-e0980c297ce8.png)

<p align="right">(<a href="#top">back to top</a>)</p>
  
  
  
<!-- CONTACT -->
## Contact

Email - ianambrose@pm.me

Project Link: https://github.com/IanAmbrose/telegram-lambda-bot-

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
