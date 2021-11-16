import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Insta Username:")

ig.download_profile(dp,	profile_pic_only = True)