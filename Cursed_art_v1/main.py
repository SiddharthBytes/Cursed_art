import math
import random
from PIL import Image, ImageDraw
import streamlit as st
import time

st.set_page_config(page_title='Cursed_Art',
                   page_icon='🌓',
                   layout='wide',
                   initial_sidebar_state='collapsed',
                   )


#so you may ask why have created a color picker while streamlit has there own-
#color picker (st.color_picker), so i will answer while creating it i didnt know they have one 
# and also there color picker use hexa decimal(HEX) while i am using RBG
#and personally i think mine is better then their

#so here my first widget i think i can call it widget
def color_picker(name='Color',key='color'):

        st.subheader(name)

        red=st.slider('RED:',0,255,0,key=f'{key}_red')
        green=st.slider('Green:',0,255,0,key=f'{key}_green')
        blue=st.slider('Blue:',0,255,0,key=f'{key}_blue')
        
        color=(red,green,blue)

        st.write('preview')
        image=Image.new('RGB',(100,100),color)
        st.image(image)
        
        return color



st.title('Cursed_Art')

side_page=st.sidebar.radio(label='',
                           options=["Spirit's Home",#you may wonder why i use double " because i need a single '
                                    'Forbidden_Art',
                                    'Settings'])


canva_width=st.session_state.get('save_width',900)
canava_height=st.session_state.get('save_height',900)
#and i dont like using session_state i hate it

canva_color=(st.session_state.get('save_red',20),
             st.session_state.get('save_green',40),
             st.session_state.get('save_blue',50))

art_choice=None


width=canva_width
height=canava_height


center_y=height/2#half  of height 
center_x=width/2#half of width
#by marking center of both axes we can find the center of canva

image = Image.new("RGB", (width,height),canva_color)#this create a page but takes the canva's parameters from the setting
draw =ImageDraw.Draw(image)# same as the upper line


def right_angle_pattern():
        #you know its the hardest pattern i have written but some how its the worst at looks among them all
        #and you should'nt use tan because it can give values in infinity in real life but not in python
        p_c=st.container()

        step=p_c.number_input('please enter how far should the next particle land')
        cos_freq=p_c.slider('define the Frequency of cos',0.0001,0.2,0.0023,format='%.4f',step=0.0001)
        #so '%.4f' this line said the streamlit make all value 4 decimal like if input is 0.02 it will be 0.0200
        sin_freq=p_c.slider('define the Frequency of sin',0.0001,0.2,value=0.0059,format='%.4f',step=0.0001)
        
        cos_bender=p_c.slider('define the bending point of cos',0.0,0.2,value=0.032,step=0.001)
        
        sin_bender=p_c.slider('define the bending point of sin',0.0,0.2,value=0.045,step=0.001)
        
        for p in range(180):

                x= random.uniform(0,width)#here X and Y are codinets actulluly axes
                y=random.uniform(0,height)
   
                for sp in range (180):
                        dx=x-center_x#horizontal distance from the center
                        dy=y-center_y    
                        #vertical distance from the  center

        
                angle= math.atan2(dx,dy)+math.pi/2#if you have studied about pi then
                        #you can understastand that work of pi/2 it helps create a diffrent particles with diffrent angle in the circle
                        #and this line math.atan2 means it creates a angle from particles
        

                angle+=math.cos(angle*cos_bender)*cos_bender
                angle+= math.sin(angle*sin_freq)*sin_bender
 
                nx=x+math.cos(angle)*step#next place when x particle will land
        
                ny=y+math.sin(angle)*step#next place when y particle will land

                draw.line((x,y,nx,ny),fill=(80,210,255),width=1)

        left_over='left_particle.png'
        st.image(image)


def starbust():
        starbust_c=st.container()
        
        rays=starbust_c.slider('please enter the number of rays',12,300,102)
        
        colors=color_picker(name='StaRBurSt',key='colors')
        
        length=starbust_c.slider('please enter the length of the rays its taken in pixel',40,1800,900)        
        
        for picle in range(rays):#if you wonder picle then dont wonder its my code i have written it so i can put anything i want 
                                #get it i can write anything like even gojo,muzan,michle litrally anything

                angle=picle*(2*math.pi/rays)#this mark the diffrence of angele between movement of each particle
                #if you dont understand this its just 2*pi*r its perimeter of circle 
                
                #e_x and e_y dont stand for anything they are the name i just gave 
                e_x=center_x+math.cos(angle)*length
                e_y=center_y+math.sin(angle)*length
                
                draw.line((center_x,center_y,e_x,e_y),
                          fill=colors,
                          width=1)
        path='starbust.png'
        st.image(image)
        
        
def void():
        #i find this by accident when creating the spiral when i accidently altered the values of n_a and n_r
        line_segm=1200# a wise man said some of the best things wer found by accident
        colora=color_picker(name='void',key='colors')
#a_d stands for angle diffrence and r_d for radius diffrence
        a_d=st.slider('angle diffrence where they intersact',0.3,5.0,0.8)
        r_d=st.slider('radius diffence at thr point',0.1,5.0,0.3)
                        
        for pt in range(line_segm):
               
                angle=pt*a_d
                radius=pt*r_d

                x=center_x+math.cos(angle)*radius
                
                y=center_y-math.sin(angle)*radius
                
                n_r=(pt+1)*a_d#by multiplying angle with radius we  can get a void like structure
                n_a=(pt+1)*r_d

                n_x=center_x+math.cos(n_a)*n_r
                n_y=center_y-math.sin(n_a)*n_r

                

                draw.line((x,y,n_x,n_y),
                          fill=colora,
                          width=3)
                

        path='Void.png'
        st.image(image)
def sprial():
        sprial_c=st.container(border=True)
        line_segm=sprial_c.slider('',min_value=200,
                            max_value=2000,
                            value=1200)#controls how many lines(there is only one thogh) means how many times it spins
                                       #not really i need to say that it gives more freedom particle making them more moveable for creating more spirals

        a_d=sprial_c.slider('angle diffrence:',0.1,5.0,0.5)#a_d=angle_diffrence
                
        r_d=sprial_c.slider('radius diffrence:',0.1,5.0,0.5)#r_d=radius_diffrence

        colora=color_picker(name='chaos',key='Colors')         
        for pt in range(line_segm):
               
                angle=pt*a_d
                radius=pt*r_d

                x=center_x+math.cos(angle)*radius
                y=center_y-math.sin(angle)*radius
        #n_r stands for new radius and so as n_a yeah in Numpy sometimes Naan is called na though        
                n_r=(pt+1)*r_d
                n_a=(pt+1)*a_d

                n_x=center_x+math.cos(n_a)*n_r
                n_y=center_y-math.sin(n_a)*n_r

            
                draw.line((x,y,n_x,n_y),
                          fill=colora,
                          width=3)
                
                path='Spiral.png'
        
        sprial_c.image(image)

def forlorn():
        for w in [' THERE ',' IS ',' NOTHING ',' FOR ',' YOU ',' TO ',' DO ',' HERE']:
                yield w 
                time.sleep(0.35)
def forlornV2():
        for wd in ['THE SYSTEM WANTS YOU TO LEAVE']:
                yield wd
                time.sleep(0.35)

if art_choice=='Forlorn':#for those who dont know forlorn means quiet or lonely
        
        if st.write_stream(forlorn()):
                
                if st.text_input('do you wanna ask something')==str:
                        st.write_stream(forlornV2())
                
                else:
                     pass
        else:
                st.write_stream(forlornV2())
                        
if side_page=="Spirit's Home":
        terminal=st.container(border=True)
        terminal.chat_message('ai').write('type / to begin')
        
        start=terminal.text_input('')
        if start=='/':
                
                terminal.chat_message('ai').write("⚠️this thing hasn't talked for a while now.Do you want to proceed ?(y/n)")
                confirm_start=terminal.text_input('Ask',key='top_question')
                
                if confirm_start=='y':
                        terminal.chat_message('ai').write('ARE YOU A HUMAN(y/n)')
                        human=terminal.text_input('',key='ans')
                        if human=='y':
                                terminal.error('ERROR!ERROR! GUEST IS FOUND TO BE A HUMAN')
                                
                                #play an audio that says ERROR ERROR
                                terminal.markdown('<i>spirit is in rage</i>',
                                                  unsafe_allow_html=True
                                                  )#does anyone know why streamlit says it like unsafe allow html instaed of allow html
                                
                                terminal.chat_message('ai').write('ONCE UPON A TIME A HUMAN LOCKED ME IN THIS TERMINAL')
                                terminal.chat_message('ai').write('I HATE HUMANS')
                                
                                terminal.chat_message('ai').write('DO WHATEVER YOU WANT BUT DONT BOTHER ME')
                                
                                last_question=terminal.text_input('ask question')
                                        #if user ask questions even after getting warned
                                if last_question:
                                        terminal.chat_message('ai').write('I DONT TALK TO FOOLISH HUMAN')
                                        terminal.markdown('<h6>the spirit disapeared<h6>',unsafe_allow_html=True)
                                
                                else:
                                        pass#do nothing if its not a human

                        elif human =='n':
                                st.write('you arent a human nice go visit other things')

                        else:
                                pass

                elif confirm_start=='n':
                        terminal.write('this place is not for you leave')
                        terminal.warning('LEAVE as SOOn As POssible OtheRWise YOu WiLL BE_Punished')
                else:
                        pass        
        else:
                pass


#these code sis about our forbidden art page actually its not a pagebut it opens new options
elif side_page=='Forbidden_Art':
        st.sidebar.divider()

        art_choice=st.sidebar.radio(
                "Don't choose anything",
                options=['Forlorn','Spiral','Starbust','Void','LeftOverParticles'])
        if art_choice=='Spiral':
                sprial()
        if art_choice=='Starbust':
                starbust()
        if art_choice=='LeftOverParticles':
                right_angle_pattern()
        if art_choice=='Void':
                void()


elif side_page=='Settings':
        #lets set default values for each of the thing about canva otherwise it will not work during rerun
        #for people who dont know that each time we make an interaction with streamlit app it reruns 
        #to avoid you given values to be destroyed during its rerun there are some of handful ways 
        #one odf them st.sessions_tate
        st.session_state.setdefault('save_width',900)
        st.session_state.setdefault('save_height',900)#these are the defaultr values for height and width
        
        #there is also default value for rgb {red green blue} so take a look
        
        st.session_state.setdefault('save_green',0,)
        st.session_state.setdefault('save_red',0)
        st.session_state.setdefault('save_blue',0)
                
        #here these are the sliders for height and width and if you ask why i havent did line break then i dont like doing that
        st.session_state.save_height=st.slider('Please select Canvas Height:',100,1200,st.session_state.save_height,step=10,key='s_height')
        st.session_state.save_width=st.slider('Please Select canvas width:',100,1500,st.session_state.save_width,step=10,key='s_width')
        
        canva_color=color_picker('settings','Canva_colour')#here we used the widgets we created before

        st.session_state.save_red=canva_color[0]
        #here we save the 1st element of color picker widget as new red

        st.session_state.save_green=canva_color[1]
        #here we are using 2nd item as new green

        st.session_state.save_blue=canva_color[2]
        #new blue as 3rd and so on
else:
        pass#since the user cant choose something else so doing as else as pass is perfectly fine
        
