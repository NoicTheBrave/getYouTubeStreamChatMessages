# getYouTubeStreamChatMessages
Trying to figure out a way to get my channel's YT stream messages from whatever stream I want w/o having to update the URL every time or use API calls 


Currently, I am just webscraping this information: 

Required Software
* Python ver. 3.11 of higher (whatever is compatable with this thing) 
* [Selenium](https://pypi.org/project/selenium/) - Loads the webpages in the background for those "dynamic" things you need to tell if one someone's main YT page is they're streaming (webpage must be loaded to generate that inf0) (ver 4.28.1)
* Google Chrome (used ver. 132.0.6834.111 for this test, but not required) - Must be installed on your computer (I think) in order for this to work properly (Check Version: Settings -> About Chrome)\
* [Chrome Drivers](https://developer.chrome.com/docs/chromedriver/downloads) - This is why you need to know what ver. of chrome you have so Selenium can use it to access the web. [You may need to use this link if the other one isnt working](https://googlechromelabs.github.io/chrome-for-testing/#stable) (yes, it looks sketchy, but trust me, its fine!)




