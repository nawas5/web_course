
import pandas as pd
import plotly.express as px
import plotly.io as pio

the_years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003",
             "2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

df = pd.read_csv("Gender_StatsData.csv")
df = df[(df["Indicator Name"]=="Expected years of schooling, female")|\
        (df["Indicator Name"]=="Expected years of schooling, male")]
df = df.groupby(["Country Name","Country Code","Indicator Name"], as_index=False)[the_years].mean()


world=["Arab World","South Asia","Latin America & Caribbean","East Asia & Pacific","European Union"]
world_xrange=[4,19]


# ------------------------------------------------------------------------------
# Choose dataframe Region and sort column
df = df[df['Country Name'].isin(world)]
df['Country Name'] = pd.Categorical(df['Country Name'], ['South Asia','Arab World','East Asia & Pacific',
                                                         'Latin America & Caribbean',"European Union"])
df.sort_values("Country Name", inplace=True)

df = pd.melt(df,id_vars=['Country Name','Country Code','Indicator Name'],var_name='Year',value_name='Rate')


# ------------------------------------------------------------------------------
# Build the dot plot (variation of scatter plot)
fig = px.scatter(df, x="Rate", y="Country Name", color="Indicator Name", animation_frame="Year",
                 range_x=world_xrange, range_y=[-0.5,5.0],
                 title="Gender Gaps in our Education",
                 labels={"Rate":"Years a child is expected to spend at school/university",
                        "Indicator Name":"Gender"} # customize label
      )
fig.update_layout(title={'x':0.5,'xanchor':'center','font':{'size':20}},
                  xaxis=dict(title=dict(font=dict(size=20))),
                  yaxis={'title':{'text':None}},
                  legend={'font':{'size':18},'title':{'font':{'size':18}}})


fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 800

fig.data[0].name = 'Girl'
fig.data[1].name = 'Boy'

fig.data[0]['marker'].update(size=14)
fig.data[1]['marker'].update(size=14)

fig.data[0]['marker'].update(color='#22bc22')
fig.data[1]['marker'].update(color="#fda026")

for x in fig.frames:
    x.data[0]['marker']['color'] = '#22bc22'
    x.data[1]['marker']['color'] = '#fda026'

pio.show(fig)