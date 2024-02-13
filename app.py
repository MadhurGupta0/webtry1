import streamlit as st
import requests as res
#from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image


def main():
  st.set_page_config(page_title="Maddy website",page_icon="🫥", layout="wide")
  current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
  image = Image.open(current_dir/"image"/"img.PNG")

#____ header _____
  with st.container():

    st.subheader("Hi,I am Maddy 😊")
    st.title("this is just a fun project")
    st.write ("Welcome,This is link to my "+"[linkden account>](https://colab.research.google.com/drive/1igmiGImbaNTiWRdJ0EQknAzKG_iDCoGh?authuser=0#scrollTo=8-lCreENOKrU)")
#-------
 # lottie_ff= lottie_url("https://lottie.host/f50a4fa7-89d1-424a-94db-0bfc3fd58488/RzZloYluvQ.json")
  with st.container():
      st.write("---")
      lcol,rcol=st.columns(2,gap="large")
      with lcol:
          st.header("[thes are some poplur sites](https://colab.research.google.com/drive/1igmiGImbaNTiWRdJ0EQknAzKG_iDCoGh?authuser=0#scrollTo=8-lCreENOKrU)")
          st.write("##")
          st.write("""
          this is just some gibres since I lack creatvity :
          - this is good oppurtunity to to ftell abot my self 
          - I am maddy an soft ware enginer
          - I am just tring to to learn from this code.
          - And I so lack creativit so i can not even think any further 
           
          """)
          st.write("[you can click on an suspious link](https://colab.research.google.com/drive/1igmiGImbaNTiWRdJ0EQknAzKG_iDCoGh?authuser=0#scrollTo=8-lCreENOKrU)")
     # with rcol:
     #    st_lottie(lottie_ff,height=400,key="random")
  with st.container():
          st.write("---")
          st.header("A random photo to comment")
          st.write("##")
          icol,tcol=st.columns((1,2))
          with icol:
              st.image(image)

          with tcol:
              st.subheader("COMMENTS")
              st.write("""
              xxy: this is all b s.
              """)
              comment=st.text_input("yours")
              if st.button("🦐"):
                  st.write(f"MADDY : {comment}")
              st.markdown("[image source...](https://genshin.hoyoverse.com/en)")


#def lottie_url(url):
 #   r= res.get(url)
  #  if r.status_code != 200:
   #     return None
    #return r.json()


if __name__=="__main__":
    main()
