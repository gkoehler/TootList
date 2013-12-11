# How it Should Work

Example: I want to send 3 tweets per day, at random times between
6am and 11pm. 

Every time I make a new tweet, I want it to fill in the next available "slot" (after the last one), unless I specify a time for it to run. 

Tweets need to be posted within the next 5 minutes.

So, django-cron won't be much use to me. 

Instead, schedule a management command to run every 5 minutes, which would check for toots and post them.

In order to auto-queue tweets, I need to know the `hours_allowed`, and `tweets_per_day`. 

`Hours_allowed` should be checkboxes (or multi-select), telling me the on/off times for scheduling posts. 

Users should be able to checkbox a bunch of tweets and "shift" them to a new date. "Move to End of Queue," maybe. Should also have, "Move to First Available Slots."

Should also be able to bulk-upload a list of tweets from a text file.

Published toots should be deleted once they are posted. Once this is implemented, we won't need the 'published' attribute.

## What to Build First

1. Function for scheduling next random date/time for posting
1. Function for calculating tweets to post "now"
1. Model + admin for creating twitter account
	* Fixture for `TimeToRun` objects. Generate via admin interface.
1. Model + admin for entering tweets
1. Function for checking #4 and then posting tweet
1. Management command for #5
1. Bulk upload and additional actions
