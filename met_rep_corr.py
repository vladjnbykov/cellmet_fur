################# INTERNAL TIMING ######################
from matplotlib.collections import PathCollection
import streamlit.components.v1 as stc
from math import pi
import ppscore as pps
import seaborn as sns
import plotly.express as px
import codecs
import statsmodels
from PIL import Image
from palettable.colorbrewer.qualitative import Pastel1_7
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
startTime = time.time()
########################

# wide screen layout
st.set_page_config(layout="wide")


def render_html(file, height=700, width=700):
    html_file = codecs.open(file, 'r')
    page = html_file.read()
    stc.html(page, width=width, height=height, scrolling=True)


stc.html("""<h1 style='color:blue; font-size:24px; margin-top:0; margin-bottom: 2px;'>
	5-Fluorouracil family in translational reading through p53 premature termination codons:
	opportunities for cancer treatment.</h1>""", height=60)

stc.html("""<h4 style='color:rgb(30,0,200); font-size:1em; margin-top:0;'>
	Interactive dashboard to the paper by Mireia Palomar-Siles et al. under title “5-Fluorouridine induces 
	functional full-length p53 in nonsense mutant human tumor cells”</h4><br>""", height=60)

c1, c2, c3 = st.columns([5, 1, 5])
with c1:
    image = Image.open('./images/FU_western.png')
    st.image(image, width=300)

with c2:
	st.write('')

with c3:
    stc.html("""<h4 style='color:rgb(30,0,200); font-size:0.75em; text-align:justify; margin-top:0; margin-bottom: 10px; padding-left:5px;'>
	Suppression of premature termination codon in p53 in cells by 5-FU as evident by emergence of 
	50kDa band in concentration and time-dependent manner according to the Western blotting</h4>""", height=50)

stc.html("<h3 style='color:rgb(30,0,200); margin-top:0;'>Metabolic profile</h4>", height=30)


def main():

    # INTRO button
    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter():
        st.session_state.count += 1
        if st.session_state.count % 2 != 0:
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
				<strong>Introduction</strong><br><br>
				In the field of cancer therapy, the main problem is tumour resistance to the applied 
				treatment. It is primarily associated with a priori tumour genetic background leading
				to tumour genetic instability and thus high plasticity under the applied treatment. 
				Mutations, alterations to the genetic material, in a few genes are associated with 
				resistance to current therapeutic interventions. One of such prominent genes in this 
				collection is p53 which is mutated in nearly half of all human tumours. Going down 
				one more layer into the complexity, there are different types of mutations, missense, 
				leading to the production of mutant protein and nonsense, introducing a premature 
				termination codon into DNA. Such premature termination codons during protein synthesis 
				result in the expression of a truncated protein which usually lacks its original function. 
				For p53 it is tumour suppression and sensitivity to a number of anti-cancer treatments. 
				Thus, suppression of these premature termination codons will restore original anti-tumour 
				activity of p53 and therefore tumour sensitivity to an applied therapy.<br><br> 
				The data presented here show results of several experiments which help to understand 
				mechanism of activity of the tested compounds and how it is related to suppression of 
				premature termination codons and biological effect targeting cells with nonsense 
				mutations in p53 tumoursuppressor gene. The information is in the interactive format 
				which enables a reader to actively interact with data and draw own conclusions which 
				might not be identical to the conclusions which are put forward by the researchers. 
				This is supplementary information to the paper published by Mireia Palomar-Siles et al. 
				under title “5-Fluorouridine induces functional full-length p53 in nonsense mutant human 
				tumor cells”.<br><br>
				Here the following experiments are presented:<br></p>
				<ul>
					<li>Metabolic pattern of the tested substances, 5-Fluorouracil (5-FU), 5-Fluorouridine 
					(5-FUR), 5-Fluorodeoxyuridine (5-FdUR), G418 and pseudouridine. Measurements of the 
					substances presented in the radar plots are done in the media on the day of treatment 
					(day 0) and during next three days. For cellular metabolism measurements were done 
					after 1,2 and 3 days of the treatment. Samples were analysed by LC-MS. Radar plot 
					presents scaled data since molar concentrations of substances varied by several orders 
					of magnitude from each other.</li><br>
				
					<li>Pattern of uridine species in RNA. After 3 days of incubation with a respective 
					substance, total RNA was extracted. The bulk fraction contained species longer that 
					200 bases and comprises mainly (over 85%) of ribosomal RNA (rRNA), then from that 
					fraction messenger RNA (mRNA) was purified.</li><br>

					<li>Tumour cell lines with vectors either carrying empty cassette or loaded with p53 
					cDNA harbouring a premature termination codon were compared in terms of their 
					biological responses to the treatment with tested substances. The response was estimated 
					either as ratios between IC50: s (concentration of a substance which supresses cell 
					growth by 50%) in loaded vs empty vector cells. This comparison gives information whether 
					the applied treatment preferentially target cells harbouring nonsense mutations. The 
					higher the ratio, the stronger effect in nonsense- mutated cells.</li><br>

					<li>Results of Western blotting where proteins extracted from cells are resolved on a 
					gel based on their molecular mass, transferred to a membrane and then probed with 
					antibodies against targets of interest. Here samples of tumour cells carrying vector 
					loaded with nonsense- mutated p53 were either control mock-treated or treated with 
					the tested substances. The image shows a band corresponding to p53 molecular size and 
					recognized with anti-p53 antibodies that appears upon treatment with fluorinated 
					analogues of uracil and G418. Thus, here we see indication that premature termination 
					codons were suppressed by the experimental treatment.</li><br>
				
				</ul>
				 
					<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
					<strong>Metabolism of fluorinated species of uracil</strong><br><br>
					The first analogue of fluorinated uracil, 5-Fluorouracil (5-FU), was developed in 
					1950s and soon started to be used in cancer chemotherapy. Here we have studied 
					5-FU and several it’s analogues, 5-Fluorouridine, 5-Fluorodeoxyuracil. They all 
					are interconvertible to each other thus having a lot in common in their effects 
					in cells. However, there are some differences in the preferential targets because 
					interconversion is slow.<br><br>
					Here is a figure showing relationship between these chemicals and the known 
					biochemical effects they exert. 
					</p>""", height=1100)
            col1, col2, col3 = st.columns([1, 6, 1])
            with col1:
                st.write('')
            with col2:
                image = Image.open('./images/FU_met.jpg')
                st.image(image, width=520)
            with col3:
                st.write('')
        else:
            stc.html("""<p></p>""", height=0)
    st.sidebar.button('INTRO', on_click=increment_counter)

    # RadioButtons
    status = st.sidebar.radio("Select treatment", ("control", "G418",
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
    time_sel = st.sidebar.slider("Duration of treatment, days", 0, 3)

    st.success("{} treatment for {} day(s)".format(status, time_sel))

    # Layout for introductory columns
    left_column, right_column = st.columns((1, 3))
    with left_column:
        # Show structural formula of the selected compound
        if tr_sel == "G418":
            image = Image.open('./images/G418.png')
            st.image(image, width=150)
        elif tr_sel == "5-FU":
            image = Image.open('./images/Fluorouracil.png')
            st.image(image, width=80)
        elif tr_sel == "5-FUR":
            image = Image.open('./images/Fluorouridine.png')
            st.image(image, width=120)
        elif tr_sel == "5-FdUR":
            image = Image.open('./images/FdUR.png')
            st.image(image, width=120)
        elif tr_sel == "PSU":
            image = Image.open('./images/Pseudouridine.png')
            st.image(image, width=120)

    with right_column:
        # Short description of the tested substances
        if tr_sel == "G418":
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
			<a style='text-decoration: none; font-weight: bold;' href = 'https://en.wikipedia.org/wiki/G418', 
			target='_blank'>G418/geneticin</a>, 
			aminoglycoside antibiotic, blocks polypeptide biosynthesis in procariotes and eucariotes. 
			Paradoxically it also known as <a style='text-decoration: none; font-weight: bold;' 
			href = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5754804/' target='_blank'>inducer of translational 
			reading through premature termination codons </a> by binding to ribosomal 
			RNA in the ribosome decoding center.</p>""", height=120)

        elif tr_sel == "5-FU":
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
			<a style='text-decoration: none; font-weight: bold;' href = 'https://en.wikipedia.org/wiki/Fluorouracil', 
			target='_blank'>5-Fluorouracil</a>, 
			cancer medication, widely used in chemotherapy since 1950s. Mechanism of action is coupled 
			to its metabolism to Fluorouridine which incorporates into RNA 
			instead of uridine; and to Fluorodeoxyuridine which both inhibits thymidylate sythase, 
			thus blocking DNA synthesis and incorporates into DNA instead of thymidine 
			triggering DNA damage signalling cascade. Both metabolites are interconvertible</p>""", height=150)

        elif tr_sel == "5-FUR":
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
			<a style='text-decoration: none; font-weight: bold;' href = 'https://pubchem.ncbi.nlm.nih.gov/compound/5-Fluorouridine', 
			target='_blank'>5-Fluorouridine</a>, 
			active metabolite of 5-Fluorouracil, converts to Fluorodeoxyuridine and inhibits thymidylate synthase thus humpering DNA synthesis 
			and cell proliferation; and also it incorporates into RNA instead of uridine.</p>""", height=150)

        elif tr_sel == "5-FdUR":
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
			<a style='text-decoration: none; font-weight: bold;' href = 'https://pubchem.ncbi.nlm.nih.gov/compound/floxuridine', 
			target='_blank'>5-Fluorodeoxyuridine/ Floxuridine</a>, 
			active metabolite of 5-Fluorouracil, interconvertable to 5-Fluorouridine, inhibits thymidylate synthase 
			thus humpering DNA synthesis and cell proliferation; and incorporates into DNA instead of thymine and triggers 
			DNA damage signalling cascade.</p>""", height=150)

        elif tr_sel == "PSU":
            stc.html("""<p style='color:rgb(28, 0, 138); margin-top:0; padding-left:10px; text-align:justify;'>
			<a style='text-decoration: none; font-weight: bold;' href = 'https://en.wikipedia.org/wiki/Pseudouridine', 
			target='_blank'>Pseudouridine</a>, 
			structural isomer of uridine, most abundant RNA modification in human cells. Due to more rotational 
			freedom of uracil moiety it likely to have contribution to RNA structure and stability. 
			In mRNA it is known to reduce stringency of STOP codons recognition.</p>""", height=120)

    # METABOLISM IN THE MEDIA: Radar plot
    if 'df_media_sc' not in st.session_state:
        st.session_state.df_media_sc = pd.read_csv("./data/media_total_sc.csv")

    #df_media_sc = pd.read_csv("./data/media_total_sc.csv")
    labels = ['m-G418', 'm-5FU', 'm-5FUR', 'm-5FdUR', 'm-U', 'm-PSU', 'm-inosine',
              'm-GSH', 'm-glutamine']

    left_column, right_column = st.columns((1, 1))
    with left_column:

        values = st.session_state.df_media_sc.loc[(st.session_state.df_media_sc["samples"] == tr_sel) & (
            st.session_state.df_media_sc["time"] == time_sel)].values.flatten().tolist()
        values = values[2:]
        num_vars = len(labels)

        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))

        ax.plot(angles, values, color='#47009E', linewidth=1)
        ax.fill(angles, values, color='#47009E', alpha=0.1)
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles), labels)

        for label, angle in zip(ax.get_xticklabels(), angles):
            if angle in (0, np.pi):
                label.set_horizontalalignment('center')
            elif 0 < angle < np.pi:
                label.set_horizontalalignment('left')
            else:
                label.set_horizontalalignment('right')

        ax.set_ylim(0, 1)
        ax.set_rlabel_position(180 / num_vars)

        ax.tick_params(colors='#222222')
        ax.tick_params(axis='y', labelsize=8)
        ax.grid(color='#AAAAAA')
        ax.spines['polar'].set_color('#222222')
        ax.set_facecolor('#FAFAFA')

        ax.set_title('Metabolism in the medium', y=1.08,
                     fontsize=12, color="#47009E")
        fig

    # INTRACELLULAR METABOLISM: Radar plot
    with right_column:
        if time_sel != 0:

            if 'df_sc1' not in st.session_state:
                st.session_state.df_sc1 = pd.read_csv("./data/df_sc1.csv")
            #df_sc1 = pd.read_csv("./data/df_sc1.csv")
            labels = ['G418', '5-FU', '5-FUR', '5-FdUR', 'U', 'PSU', 'inosine',
                      'GSH', 'GSSG', 'glutamine']

            values = st.session_state.df_sc1.loc[(st.session_state.df_sc1["samples"] == tr_sel) & (
                st.session_state.df_sc1["time"] == time_sel)].values.flatten().tolist()
            # slice df to remove extra generated values
            values = values[2:]
            # Number of variables we're plotting
            num_vars = len(labels)

            # Split the circle into even parts and save the angles
            # so we know where to put each axis.
            angles = np.linspace(0, 2 * np.pi, num_vars,
                                 endpoint=False).tolist()
            values += values[:1]
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
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
            # Can be set gridlines manually:
            # ax.set_rgrids([20, 40, 60, 80, 100])

            # Set position of y-labels (0-1) to be in the middle
            # of the first two axes.
            ax.set_rlabel_position(180 / num_vars)

            # Change the color of the tick labels.
            ax.tick_params(colors='#222222')
            # Make the y-axis (0-1) labels smaller.
            ax.tick_params(axis='y', labelsize=8)
            # Change the color of the circular gridlines.
            ax.grid(color='#AAAAAA')
            # Change the color of the outermost gridline (the spine).
            ax.spines['polar'].set_color('#222222')
            # Change the background color inside the circle itself.
            ax.set_facecolor('#FAFAFA')

            # Add title.
            ax.set_title('Metabolism in cells', y=1.08,
                         fontsize=12, color="blue")
            fig

    # RNA COMPOSITION: DOUGHNUT CHARTS
    if (tr_sel != 'PSU' and time_sel == 3):

        if 'df_rna_ur' not in st.session_state:
            st.session_state.df_rna_ur = pd.read_csv(
                './data/ur_main_species_md.csv')

        stc.html("""<h3 style='color:rgb(30,0,200); margin-top:2px; margin-bottom:2px;'>
			RNA composition, main uridine species after 3 days of treatment</h3>""", height=40)

        left_column, right_column = st.columns((1, 1))

        with left_column:
            # rRNA DATA
            doughnut = plt.subplots(figsize=(2, 2))
            r_rna_sel = st.session_state.df_rna_ur.loc[(st.session_state.df_rna_ur["names"] == tr_sel) & (
                st.session_state.df_rna_ur["rna"] == 'rRNA'), ['uridine', 'pseudouridine', 'FUR']]
            r_rna_sel = r_rna_sel.iloc[0]

            groups = ['U ' + str(round(r_rna_sel[0], 1)) + "%",
                      'PSU ' + str(round(r_rna_sel[1], 1)) + "%",
                      '5-FUR ' + str(round(r_rna_sel[2], 1)) + "%"]

            my_circle = plt.Circle((0, 0), 0.7, color='white')
            plt.pie(r_rna_sel, labels=groups,
                    colors=Pastel1_7.hex_colors, textprops={'fontsize': 5})
            doughnut = plt.gcf()
            doughnut.gca().add_artist(my_circle)
            plt.title('rRNA', y=0.4, fontsize=10, color="blue")
            doughnut

        with right_column:
            # mRNA DATA
            doughnut1 = plt.subplots(figsize=(2, 2))
            m_rna_sel = st.session_state.df_rna_ur.loc[(st.session_state.df_rna_ur["names"] == tr_sel) & (
                st.session_state.df_rna_ur["rna"] == 'mRNA'), ['uridine', 'pseudouridine', 'FUR']]
            m_rna_sel = m_rna_sel.iloc[0]

            groups = ['U ' + str(round(m_rna_sel[0], 1)) + "%",
                      'PSU ' + str(round(m_rna_sel[1], 1)) + "%",
                      '5-FUR ' + str(round(m_rna_sel[2], 1)) + "%"]

            my_circle = plt.Circle((0, 0), 0.7, color='white')
            plt.pie(m_rna_sel, labels=groups,
                    colors=Pastel1_7.hex_colors, textprops={'fontsize': 5})
            doughnut1 = plt.gcf()
            doughnut1.gca().add_artist(my_circle)
            plt.title('mRNA', y=0.4, fontsize=10, color="blue")
            doughnut1

        # BIOLOGICAL EFFECTS: BAR CHARTS

        if (tr_sel != 'PSU' and tr_sel != 'control' and time_sel == 3):
            if 'pooled_biol' not in st.session_state:
                st.session_state.pooled_biol = pd.read_csv(
                    './data/pooled_biol.csv')

            stc.html("""<h3 style='color:rgb(30,0,200); margin-top:2px; margin-bottom:2px;'>
			Biological effects dependent on premature- termination codon</h3>""", height=40)


            left_column, right_column = st.columns((1, 1))

            with left_column:
                selector = st.session_state.pooled_biol.loc[st.session_state.pooled_biol['treatment'] == tr_sel]
                sns.set_palette("Paired")
                fig, ax = plt.subplots(figsize=(1, 1))

                ax = sns.barplot(x='treatment', y='value', hue='estimator',
                                 data=selector)
                ax.legend(fontsize=5, bbox_to_anchor=(1.05, 1),
                          loc='upper left', borderaxespad=0)

                ax.set_title('R213X- specific biological effects',
                             fontsize=8, color="blue")
                plt.ylabel('specificity, log2', size=6)
                plt.xlabel('treatment', size=6)


                for tick in ax.xaxis.get_major_ticks():
                    tick.label.set_fontsize(6)
                for tick in ax.yaxis.get_major_ticks():
                    tick.label.set_fontsize(6)


                fig

            with right_column:
                stc.html("""<p style='color:rgb(30,0,200); font-size: 12px; margin-top:2px; margin-bottom:2px; text-align:justify;'>
			These experiments shows comparison how cell lines, one carrying empty vector and the 
			other one vector loaded with p53-R213X expression cassette, respond to the treatment.
			IC50 ratio parameter is a ratio between IC50 values, IC50 of cells with empty vector 
			divided by IC50 of cells with R213X vector. The higher the ratio, the more suppression 
			of cell growth seen in R213X cells, the more cells carrying nonsense mutations are 
			sensitive to the treatment. The second parameter, specific caspase activity, is a ratio 
			caspase activity, measure of cell death, at day 3 of the treatment between R213X-cells 
			and cells with empty vector cassette. The larger the number, the greater cell death 
			occurs preferentially in R213X cells. Negative values, we have log2 transformed data, 
			indicate preferential effect in cells carrying empty cassette. 
			</p>""", height=340)

    # Beta Expander: SELECT EDA
    df = pd.read_csv("./data/c_met_final.csv")
    df = df.drop(["Unnamed: 0"], axis=1)
    df_var1 = df.drop(["samples", "time"], axis=1)

    with st.sidebar.expander("Exploratory Data Analysis"):
        status_eda = st.radio("select EDA", ("none", "correlation", "predictive power score",
                                             "regression"))
    if status_eda == "none":
        st.error(" ")
    elif status_eda == "correlation":
        stc.html(
            "<h4 style='color:rgb(30,0,200);'>Correlation matrix on raw data</h4>", height=40)
        fig, heat = plt.subplots(figsize=(11, 4))
        heat = sns.heatmap(df_var1.corr(), annot=True,
                           fmt=',.2f', cmap="magma")
        fig

    elif status_eda == "predictive power score":
        stc.html(
            "<h4 style='color:rgb(30,0,200);'>Predictive power score</h4>", height=40)

        fig, heatmap_pps = plt.subplots(figsize=(11, 4))
        matrix_df = pps.matrix(df_var1)[['x', 'y', 'ppscore']].pivot(
            columns='x', index='y', values='ppscore')
        heatmap_pps = sns.heatmap(
            matrix_df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True, fmt=',.2f')
        fig
        stc.html("""<p style='color:rgb(30,0,200);'>The predictive power score is an asymmetric
		 score that detects linear and non-linear relationships between variables including categorical. 
		 It ranges from 0 (no prediction) to 1 (best score).</p>""")

    elif status_eda == "regression":

        stc.html(
            "<h4 style='color:rgb(30,0,200);'>Linear regression model</h4>", height=40)

        param = ['c-G418', 'c-5-FU', 'c-FUR', 'c-FdUR', 'c-U',
                 'c-PSU', 'c-inosine', 'c-GSH', 'c-GSSG', 'c-glutamine']

        X = st.selectbox("Select X", param)
        Y = st.selectbox("Select Y", param)

        fig = px.scatter(df_var1, x=X, y=Y, trendline="ols")
        fig

    else:
        st.error(" ")

    with st.sidebar.expander("Contact and acknowledgement"):

        stc.html(
            "<h4 style='color:rgb(0,0,250);'>Developer:<br>Vladimir JN Bykov, MD PhD</h4>", height=70)
        stc.html(
            "<a href = 'https://www.linkedin.com/in/vladimir-bykov-04912165/' target='_blank'>LinkedIn</a>", height=30)
        stc.html(
            "<a href= 'mailto: vlad.jnbykov@gmail.com'>Send E-mail</a>", height=30)

    ##############################
    executionTime = round((time.time() - startTime), 2)
    st.write('Script execution time in seconds: ' + str(executionTime))
    ##############################


if __name__ == "__main__":
    main()
