from .azure_util import sentiment_analysis

def analyze_sentiment(paragraph):
    return sentiment_analysis(paragraph)['documents'][0]['score']

if __name__ == '__main__':
    text = 'After worries about higher interest rates sparked a steep sell-off in early October and again on Thursday, the S & P 500 remains down 5 percent from its Sept. 20 record high close, with top-shelf stocks including Amazon.com Inc(AMZN.O), Alphabet Inc(GOOGL.O), Accounts Payable Netflix Inc(NFLX.O) and Facebook Inc(FB.O) showing little of their vitality from recent years.A quarterly report from Microsoft Corp(MSFT.O) on Wednesday after the bell, followed by Alphabet and Amazon late on Thursday, will influence sentiment across Wall Street.“The equity market is at a critical point here, ” said Kurt Brunner, portfolio manager, Swarthmore Group in Philadelphia, Pennsylvania. “In order for it not to get a lot worse, I think you need to see Amazon and Alphabet put up some good numbers.”With investors worried about increased internet regulation and criticism of Facebook’s handling of user data, the social media company’s stock has slumped 29 percent from its record high on July 25. Alphabet is 15 percent below its July 26 record high close, while Amazon has fallen 12 percent this month.'
    a = analyze_sentiment(text)
    print('dank')