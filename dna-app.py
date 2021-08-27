####################
#Import the libraries
import pandas as pd 
import streamlit as st
import altair as alt
from PIL import Image

#####################
#PAGE TITLE
#####################

#image = Image.open('d')

#st.image(image, use_column_width=True)

st.write("""
    # DNA Nucleotide Count Web APP
This aplicaction counteing the nucleotide composittion of query DNA!

***
"""
)

#########
#Input the text Box
#########

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query\n"

sequence = st.text_area("Sequence input", sequence_input, height=230)
sequence = sequence.splitlines()
sequence = sequence[1:] #Skips the name of the sequence
sequence = ''.join(sequence)

st.write("""
***
""")

# Print the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

##DNA nucleotide count 
st.header('OUTPUT (DNA Nucleotide count)')


### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())
X

### 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### 3. Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) 
)
st.write(p)