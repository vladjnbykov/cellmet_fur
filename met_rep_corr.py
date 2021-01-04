import streamlit as st 
import streamlit.components.v1 as stc
import pandas as pd 
import numpy as np 
from math import pi
import ppscore as pps
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import codecs
import statsmodels

def render_html(file,height=700,width=700):
	html_file = codecs.open(file,'r')
	page = html_file.read()
	stc.html(page,width=width,height=height,scrolling=True)

#st.title("Cellular metabolism in response to treatment with drugs")
stc.html("<h1 style='color:blue;'>Cell metabolic response to treatment</h1>",height=80)
stc.html("<h4 style='color:rgb(30,0,200);'>Overview, scaled data</h4>", height = 40)

#@st.cache
def main():
	

	# RadioButtons
	status = st.sidebar.radio("Select treatment",("control","G418", 
		"5-FU", "5-FUR", "5-FdUR", "Pseudouridine"))
	if status == "control":
 		tr_sel = "control"
	elif status == "G418":
 		tr_sel = "G418"
	elif status == "5-FU":
 		tr_sel = "5-FU"
	elif status == "5-FUR":
 		tr_sel = "5-FUR" 
	elif status == "5-FdUR":
 		tr_sel = "5-FdUR" 	
	elif status == "Pseudouridine":
 		tr_sel = "PSU" 	
	else:
		tr_sel = "control" 


	# Slider 
	# Numbers (Int/Float/Dates)
	time_sel = st.sidebar.slider("Specify duration of treatment, days",1,3)

	st.success("{} treatment for {} day(s)".format(status, time_sel))

	#
	df_sc1 = pd.read_csv("df_sc1.csv")
	labels = ['G418', '5-FU', '5-FUR', '5-FdUR', 'U', 'PSU', 'inosine',
       	'GSH', 'GSSG', 'glutamine']


	values = df_sc1.loc[(df_sc1["samples"] == tr_sel) & (df_sc1["time"] == time_sel)].values.flatten().tolist()
	# slice df to remove extra generated values
	values = values[2:]
	# Number of variables we're plotting
	num_vars = len(labels)

	# Split the circle into even parts and save the angles
	# so we know where to put each axis.
	angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
	values += values[:1]
	angles += angles[:1]

	fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
	# Draw the outline of our data.

	ax.plot(angles, values, color='blue', linewidth=1)
	# Fill it in.
	ax.fill(angles, values, color='blue', alpha=0.1)
	# Fix axis to go in the right order and start at 12 o'clock.
	ax.set_theta_offset(np.pi / 2)
	ax.set_theta_direction(-1)
	# Draw axis lines for each angle and label.
	ax.set_thetagrids(np.degrees(angles), labels)
	# Go through labels and adjust alignment based on where
	# it is in the circle.
	for label, angle in zip(ax.get_xticklabels(), angles):
	  if angle in (0, np.pi):
	    label.set_horizontalalignment('center')
	  elif 0 < angle < np.pi:
	    label.set_horizontalalignment('left')
	  else:
	    label.set_horizontalalignment('right')


	# Ensure radar goes from 0 to 1.
	ax.set_ylim(0, 1)
	# You can also set gridlines manually like this:
	# ax.set_rgrids([20, 40, 60, 80, 100])

	# Set position of y-labels (0-1) to be in the middle
	# of the first two axes.
	ax.set_rlabel_position(180 / num_vars)


	# Add some custom styling.
	# Change the color of the tick labels.
	ax.tick_params(colors='#222222')
	# Make the y-axis (0-1) labels smaller.
	ax.tick_params(axis='y', labelsize=6)
	# Change the color of the circular gridlines.
	ax.grid(color='#AAAAAA')
	# Change the color of the outermost gridline (the spine).
	ax.spines['polar'].set_color('#222222')
	# Change the background color inside the circle itself.
	ax.set_facecolor('#FAFAFA')

	# Add title.
	#ax.set_title('Cell metabolic response', y=1.08, fontsize = 10, color = "blue")

	fig

	# Beta Expander: SELECT EDA

	df = pd.read_csv("c_met_final.csv")
	df = df.drop(["Unnamed: 0"], axis = 1)
	df_var1 = df.drop(["samples", "time"], axis = 1)


	with st.sidebar.beta_expander("Exploratory Data Analysis"):
		status_eda = st.radio("select EDA",("none", "correlation","predictive power score", 
		"regression"))
	if status_eda == "none":
		st.error(" ")
	elif status_eda == "correlation":
		stc.html("<h4 style='color:rgb(30,0,200);'>Correlation matrix on raw data</h4>", height = 40)
		fig, heat = plt.subplots(figsize = (11,4))
		heat = sns.heatmap(df_var1.corr(), annot=True, fmt= ',.2f', cmap = "magma")
		fig

	elif status_eda == "predictive power score":
		stc.html("<h4 style='color:rgb(30,0,200);'>Predictive power score</h4>", height = 40)

		fig, heatmap_pps = plt.subplots(figsize = (11,4))
		matrix_df = pps.matrix(df_var1)[['x', 'y', 'ppscore']].pivot(columns='x', index='y', values='ppscore')
		heatmap_pps = sns.heatmap(matrix_df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True, fmt= ',.2f')
		fig
		stc.html("""<p style='color:rgb(30,0,200);'>The predictive power score is an asymmetric
		 score that detects linear and non-linear relationships between variables including categorical. 
		 It ranges from 0 (no prediction) to 1 (best score).</p>""")

	
	elif status_eda == "regression":
		
		stc.html("<h4 style='color:rgb(30,0,200);'>Linear regression model</h4>", height = 40)
		
		param = ['c-G418', 'c-5-FU', 'c-FUR', 'c-FdUR', 'c-U',
       	'c-PSU', 'c-inosine', 'c-GSH', 'c-GSSG', 'c-glutamine']

		X = st.selectbox("Select X",param)
		Y = st.selectbox("Select Y",param)

		fig = px.scatter(df_var1, x= X, y= Y, trendline="ols")
		fig

	else:
		st.error(" ")	

	
	with st.sidebar.beta_expander("Contact and acknowledgement"):
		stc.html("<h4 style='color:rgb(0,0,250);'>Vladimir JN Bykov, MD PhD</h4>", height = 50)
		stc.html("<a href = 'https://www.linkedin.com/in/vladimir-bykov-04912165/' target='_blank'>LinkedIn</a>", height = 30)	
		stc.html("<a href= 'mailto: vlad.jnbykov@gmail.com'>Send E-mail</a>", height= 30)


if __name__ == "__main__":
	main()

