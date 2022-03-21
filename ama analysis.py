import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Analysing the data
def analysis():
    data = pd.read_excel(r'C:\Users\Reggie\PycharmProjects\pythonProject1\api understanding\ama governor youtube data.xlsx')
    del data['Unnamed: 0']
    del data['video_id']
    data = data.sort_index(ascending= False)
    data = data[[ 'creator','publish_date', 'video_name', 'views', 'likes','comments']]
    print(data.to_string())

    # total views in the  first 3 months
    first_three_months = data.loc[data['publish_date'] > '2021-12-15']
    first_view_count = first_three_months['views'].sum()

    # last 3 months
    last_three_months = data.loc[(data['publish_date'] > '2021-09-27')
                                 & (data['publish_date'] < '2022-01-09')]
    last_view_count = last_three_months['views'].sum()
    if first_view_count > last_view_count:
        gain = abs(first_view_count - last_view_count)
        print('you gained ', gain, 'views more in january, december and february')
    elif last_view_count > first_view_count:
        gain = abs(first_view_count - last_view_count)
        print('you gained',gain,'views more than the previous months')
    else:
        print('No gain')

    # line graph to show
    plt.subplots(figsize= [10,6])
    plt.plot(last_three_months['views'], 'b')
    plt.plot(first_three_months['views'],'r')
    plt.xlabel('Posts', fontsize=15)
    plt.ylabel('Views count', fontsize=15)
    plt.title('Quarterly views review(October-March)', fontsize=20)
    plt.annotate('LOYALTY TEST ON UNIVERSITY STUDENTS\nthey failed miserably\n ft @Marintia Eiko', xy=(3.03,62000) ,fontsize=10, xytext=(4,60000) ,
    arrowprops=dict(facecolor='blue'), color='green')
    plt.annotate('Do Women Actually Enjoy Backshots?\nS€X Ed w/ Ama Pt.3\n(VLOGMAS DAY 6)', xy=(19.02,137000) ,fontsize=10,
    xytext=(22, 130000), arrowprops=dict(facecolor='red'), color='green')
    plt.figtext(0, 0, 'A retrogression of views by 472,196', fontsize=15)
    plt.show()

    # the video with high views in the last six months
    six_months = data.loc[data['publish_date'] > '2021-09-27']
    average= six_months[['views', 'likes', 'comments']].mean()
    print('On a video ama governor has an average of: ')
    print(average)
    view_highest = six_months['views'].max()
    print(view_highest)
    print(' Your most viewd video was Do Women Actually Enjoy Backshots?| S€X Ed w/ Ama Pt.3 (VLOGMAS DAY 6)\n giving you about ', view_highest ,'views')
    likes_highest = six_months['likes'].max()
    print(' Your most liked video was the LOYALTY TEST ON UNIVERSITY STUDENTS, they failed miserably🤣 ft @Marintia Eiko\n giving you about ',  likes_highest, 'likes')
    comment_highest = six_months['comments'].max()
    print('your most interactive video was Your man got me pregnant and gave me an STD’ PRANK CALLS on Ghanaian girlfriends\n giving you ',comment_highest,'comments')

    # bar chart to illustrate this
    sns.set_style('white')
    plt.subplots(figsize=[12, 6])
    plt.bar(six_months['publish_date'], six_months['likes'], color='red')
    plt.bar(six_months['publish_date'], six_months['comments'], color='blue', bottom=six_months['likes'])
    plt.xlabel(None)
    plt.xticks(fontsize=7, rotation=30)
    plt.ylabel('Metrics of likes and comments')
    plt.yticks(fontsize=10)
    plt.legend(['likes', 'comments'])
    plt.title('Likes to Comments ')
    plt.text(7, 6200, 'Average likes 2,705\nAverage comments 559', fontsize=20, color='green')
    plt.show()

    # making a new columns
    recent = six_months.copy()
    mask = recent['creator'].str.startswith('A')
    recent.loc[mask, 'pay per 1000 views'] = int(5)
    print(recent['pay per 1000 views'])
    recent['Revenue earned'] = abs((recent['views']/1000) * recent['pay per 1000 views'])
    total_earnings = recent['Revenue earned'].sum()
    print(abs(total_earnings))

    # earnings generated in 2022
    year2022 = recent.loc[recent['publish_date'] > '2021-12-15']
    total_earnings_2022 = year2022['Revenue earned'].sum()
    print(int(total_earnings_2022))

    # line graph to show

    plt.subplots(figsize=[12, 6])
    colors = sns.color_palette('pastel')
    data = year2022['Revenue earned']
    labels = year2022['video_name']
    plt.pie(data, colors=colors, autopct="%.f%%", labels=labels
            , explode=[0.05]*10, pctdistance=0.5)
    plt.title('Earnings per video', fontsize=20)
    plt.figtext(0, 0, 'For this year your total revenue so far is $1,780.00\n'
                'Your loyalty test video has been your best earning video')
    plt.show()
    # write to Excel sheet
    recent.to_excel('Ama governor youtube.xlsx')
    print('done')
analysis()

