import streamlit as st
import streamlit_space as sy



st.title('Japreo FIT')
st.subheader('BETA Version')
sy.space(lines=3)


tab1, tab2, tab3 = st.tabs(["About", "Tutorial", "Feedback"])

with tab1:
    sy.space(lines=3)
    st.header("About App")
    sy.space(lines=3)
    st.text("Japreo Fit is a fitness app that helps with making sure that you can do exericses")
    st.text("with proper form  result.")
    sy.space(lines=2)
    st.info(icon= "ℹ️",body="Features are limited since this is a demo !")

with tab3:

    sy.space(lines=3)
    st.text('If you have any request for what features you would like to see in future updates,')
    st.text('email us at garadlimahdihassan@gmail.com')
    

with tab2:
    sy.space(lines=3)
    st.header("Tutorial")
    sy.space(lines=2)
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["Step 1", "Step 2", "Step 3", "Step 4", "Must Read"])


    with tab1:

        sy.space(lines=2)
        st.subheader("Select a Workout")
        st.image(image='Tutorial Images/Screenshot (2).png')

    with tab2:
        
        sy.space(lines=2)
        st.subheader("Select an Exercise")
        st.image(image='Tutorial Images/Screenshot (3).png')

    with tab3:

        sy.space(lines=2)
        st.subheader("Click to Start")
        st.image(image='Tutorial Images/Screenshot (4).png')

    with tab4:

        sy.space(lines=2)
        st.subheader("Pop-Up Will Appear In The TaskBar")
        sy.space()
        st.text('You will be given 10 seconds to get into position')
        st.text('before the pop up appears.')
        sy.space()
        st.image(image='Tutorial Images/Taskbar_Picture-removebg-preview (1).png')

    with tab5:

        sy.space(lines=2)
        st.subheader("ESSENTIAL")
        st.text("Camera Requirements")
        sy.space(lines=2)
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            
            st.subheader("Position")
            
            st.text('')
            
            sy.space()
            st.info(icon= "ℹ️",body=" Distance between you and the camera should be ideally about 6 feet apart."
                    + " This is done in order for the AI model to be as accurate as possible "
                    + "when counting reps.")
            
            st.warning(" Perfomance will greatly drop if other people are in the view of the camera!"
                       + " Make sure that you're in the view of the camera before starting your reps.", icon="⚠️")
            
        
        with col2:
            
            sy.space(lines=6)
            st.subheader("Device")
            sy.space()
        
     
            sy.space()
            st.info(icon= "ℹ️" ,body="Currently, the app is untested on mobile phones."
                    + " Additionally, make sure you keep your PC screen at an angle of 90 "
                    + "degrees for optimal performance.")
            
            sy.space()

            st.text("Preferred device: Laptop")
        




