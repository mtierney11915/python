import streamlit as st

#Title and Header
st.title('PGA Tour Internship Application Prompt 2 Response')
st.header('Welcome to my interactive Python application! This website discusses my plan to organize a charity event for stroke awareness.')
st.divider()

st.header('Select an option below to learn more about my charity event!')
box=st.selectbox(label= 'box',options=('Overview','Why This Cause?','How I Will Execute This Event','What I Hope To Accomplish'))

#for options in box:
if box == 'Overview':
    st.write('If I were to organize a charitable event, I would center it around donating to the American Stroke Association. This association is the American leader in stroke research, advocacy, and innovation. This event would be centered around a charitable golf outing at my local course that I used to work at. The goal is for this event to attract a large field of players for a good cause. ')
if box == 'Why This Cause?':
    st.write('The reason why I would choose this cause is because of the personal impact it has had on me and my family. My Aunt and Grandma both suffered strokes and luckily survived, but had their lives forever changed. My Grandpa recently had a stroke as well, and unfortunately he did not survive it. I want to raise money for this cause to spread awareness to people about the signs of strokes, as well as how to prevent them.')
if box == 'How I Will Execute This Event':
    st.write('My goal would be to organize a charitable golf outing at my home course. I have a great relationship with the head golf pro, and would work with him to organize an outing that attracts as many people as possible. I am not just choosing a golf event because this is a PGA Tour Application, but truly believe that golf is a beautiful way to bring people together over a good cause. Aside from the golf, I would hold a reception where I go over the cause and the impact it can have on millions of lives thanks to everybodies generous donation.')
if box == 'What I Hope To Accomplish':
    st.write('Aside from raising money, I really hope to spread awareness about strokes. At the reception I would take time to go over the warning signs of a stroke and prevention. Bringing together a community of people and having a good time, while also growing the game of golf in the process.')
st.divider()
st.header('See below the code that is used to run this program!')
st.code('''import streamlit as st

#Title and Header
st.title('PGA Tour Internship Application Prompt 2 Response')
st.header('Welcome to my interactive Python application! This website discusses my plan to organize a charity event for stroke awareness.')
st.divider()

st.header('Select an option below to learn more about my charity event!')
box=st.selectbox(label= 'box',options=('Overview','Why This Cause?','How I Will Execute This Event','What I Hope To Accomplish'))

#for options in box:
if box == 'Overview':
    st.write('If I were to organize a charitable event, I would center it around donating to the American Stroke Association. This association is the American leader in stroke research, advocacy, and innovation. This event would be centered around a charitable golf outing at my local course that I used to work at. The goal is for this event to attract a large field of players for a good cause. ')
if box == 'Why This Cause?':
    st.write('The reason why I would choose this cause is because of the personal impact it has had on me and my family. My Aunt and Grandma both suffered strokes and luckily survived, but had their lives forever changed. My Grandpa recently had a stroke as well, and unfortunatley he did not survive it. I want to raise money for this cause to spread awareness to people about the signs of strokes, as well as how to prevent them.')
if box == 'How I Will Execute This Event':
    st.write('My goal would be to organize a charitable golf outing at my home course. I have a great relationship with the head golf pro, and would work with him to organize at outing that attracts as many people as possible. I am not just choosing a golf event because this is a PGA Tour Application, but truely believe that golf is a beautiful way to bring people together over a good cause. Aside from the golf, I would hold a reception where I go over the cause and the impact it can have on millions of lives thanks to everybodies generous donation.')
if box == 'What I Hope To Accomplish':
    st.write('Aside from raising money, I really hope to spread awareness about strokes. At the reception I would take time to go over the warning signs of a stroke and prevention. Bringing together a community of people and having a good time, while also growing the game of golf in the process.')
st.divider()''')