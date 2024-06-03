import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ll28NvAAhFAMrWIVZW1bIbB3f", "GN6kkjDPjPwJn2mhJ9Asykn9Y0ffwA4h8wjO4NqcyF89ENRFW7")
auth.set_access_token("1514551948116389889-VaEGiZgGYGyNVfVRtDKvq3UlIq5Ihx", "AmKWSgWhRVXXmtji55LMdJQoiotPh1Q22cxxcAjH2WlOL")

api = tweepy.API(auth)

# Get trends for a specific location (WOEID)
# For worldwide trends, use 1
trends = api.get_place_trends(id=1)

for trend in trends[0]['trends']:
    print(trend['name'])
