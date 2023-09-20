from speedtestbot import Speedtestbot
from tweetbot import Tweetbot

speedtest_bot = Speedtestbot()
speed = speedtest_bot.check_speed()
tweetbot = Tweetbot()
tweetbot.tweet(speed[0], speed[1])