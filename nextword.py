# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:43:41 2021

@author: Priya
"""
import streamlit as st

from multiapp import MultiApp
from apps import intro,result,eda_vda

app = MultiApp()

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""            
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand"  target="_blank">NEXT WORD PREDICTOR</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">HOME<span class="sr-only">(current)</span></a>
      </li>
     <!-- <li class="nav-item">
        <a class="nav-link" href="/home.app" target="_blank">RESULT</a>
      </li>
 <li class="nav-item">
        <a class="nav-link" href="/data.app" target="_blank">PLOTS</a>
      </li>-->
       <li class="nav-item">
        <a class="nav-link" target="_blank" href="https://drive.google.com/file/d/1MMuEPZYiG8y2ldVq8Pw8F11OyxQ3vx6X/view?usp=sharing">DOCUMENTATION</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



st.title('**NEXT WORD PREDICTOR**')



# Add all your application here
app.add_app("OVERVIEW", intro.app)
app.add_app("EDA / VDA",eda_vda.app)
app.add_app("PREDICTION", result.app)

#app.add_app("MODEL", model.app)
# The main app
app.run()
st.info('Credit: Created by : Priya 08, Anju 10, Sadiksha 14, Pushpa 20')




