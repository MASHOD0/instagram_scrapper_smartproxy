from sentiment_analysis import get_sentiment

# webscrapping code here 


comments = ['kuch bhi, i dont know what to say', 'horrible experience', 'wow_so_nicee']

for comment in comments:    
    output = get_sentiment(comment)
    print(f'{comment=},  {output=}')
    
    # if negative send email
    
