import numpy as np
import altair as alt
alt.renderers.enable('mimetype')
alt.data_transformers.enable('data_server')


def hist( train_df, feat = None, feat_list = None, repeat = False, title = '', n_bins = 20):
    if repeat == False:
        chart = alt.Chart( train_df).mark_bar().encode(
            alt.X( feat, type='quantitative', bin = alt.Bin( maxbins = n_bins)),
            alt.Y( 'count()', stack=False, title=''),
            alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
        ).properties(
            height=100,
            width=1300
        ).facet( 'default', columns = 1)
        return chart
    if repeat == True:
        chart_list_0 = []
        chart_list_1 = []
        chart_list_concat = []
        for feat in feat_list:
            chart_tmp_0 = alt.Chart( train_df.query('default==0')).mark_bar().encode(
                alt.X( feat, type='quantitative', bin = alt.Bin( maxbins = n_bins), scale = alt.Scale( domain = ( min( train_df[ feat].min()-1, 0), train_df[ feat].max()+1))),
                alt.Y( 'count()', stack=False, title=''),
                alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
            ).properties(
                height=100,
                width=300
            )
            chart_tmp_1 = alt.Chart( train_df.query('default==1')).mark_bar().encode(
                alt.X( feat, type='quantitative', bin = alt.Bin( maxbins = n_bins), scale = alt.Scale( domain = ( min( train_df[ feat].min()-1, 0), train_df[ feat].max()+1))),
                alt.Y( 'count()', stack=False, title=''),
                alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
            ).properties(
                height=100,
                width=300
            )
            chart_list_0.append( chart_tmp_0)
            chart_list_1.append( chart_tmp_1)
            chart_concat = chart_tmp_0 | chart_tmp_1
            chart_list_concat.append( chart_concat)
        return alt.vconcat( *chart_list_concat, title = title)
# Adopted from https://github.com/UBC-MDS/cervical-cancer-predictor/blob/main/src/cervical_cancer_data_eda.ipynb.
# Function was written by the same author of this project (Chan).

def bar( train_df, feat = None, feat_list = None, repeat = False, title = ''):
    if repeat == False:
        chart = alt.Chart( train_df).mark_bar().encode(
            alt.Y( feat, type='nominal'),
            alt.X( 'count()', stack=False, title=''),
            alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
        ).properties(
            height=100,
            width=300
        ).facet( 'default', columns = 1)
        return chart
    if repeat == True:
        chart_list_0 = []
        chart_list_1 = []
        chart_list_concat = []
        for feat, domain in feat_list:
            chart_tmp_0 = alt.Chart( train_df.query('default==0')).mark_bar().encode(
                alt.Y( feat, type='nominal', scale = alt.Scale( domain = domain)),
                alt.X( 'count()', stack=False, title=''),
                alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
            ).properties(
                height=100,
                width=300
            )
            chart_tmp_1 = alt.Chart( train_df.query('default==1')).mark_bar().encode(
                alt.Y( feat, type='nominal', scale = alt.Scale( domain = domain)),
                alt.X( 'count()', stack=False, title=''),
                alt.Color( 'default', type='ordinal', scale=alt.Scale(scheme='category10'))
            ).properties(
                height=100,
                width=300
            )
            chart_list_0.append( chart_tmp_0)
            chart_list_1.append( chart_tmp_1)
            chart_concat = chart_tmp_0 | chart_tmp_1
            chart_list_concat.append( chart_concat)
        return alt.vconcat( *chart_list_concat, title = title)

def log_func(x):
    return np.log(x+1)

def translation_funct( x):
    return x - min( x) + 1