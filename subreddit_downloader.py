import praw
import config
import urllib.request

def login_bot():
	r = praw.Reddit(username = config.username, password = config.password, client_id = config.client_id, client_secret = config.client_secret, user_agent = "Subreddit Downloader")
	return r

png_count = 0
jpg_count = 0
gif_count = 0

def run_bot(r):
	hot_submissions = r.subreddit('starwars').hot(limit=10000)
	new_submissions = r.subreddit('starwars').new(limit=10000)
	top_submissions = r.subreddit('starwars').top(limit=10000)

	opener=urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)

	download_submissions(hot_submissions)
	download_submissions(new_submissions)
	download_submissions(top_submissions)

def download_submissions(subreddit_tab):
	for item in subreddit_tab:
		if item.url.endswith(".png"):
			global png_count
			png_count+=1
			urllib.request.urlretrieve(item.url, "E:/Reddit/Pictures/Star Wars/sw png " + str(png_count) + ".png")
			print(item.url)
		elif item.url.endswith(".jpg"):
			global jpg_count
			jpg_count+=1
			urllib.request.urlretrieve(item.url, "E:/Reddit/Pictures/Star Wars/sw jpg " + str(jpg_count) + ".jpg")
			print(item.url)
		elif item.url.endswith(".gif"):
			global gif_count
			gif_count+=1
			urllib.request.urlretrieve(item.url, "E:/Reddit/Pictures/Star Wars/sw gif " + str(gif_count) + ".gif")
			print(item.url)

r = login_bot()
run_bot(r)