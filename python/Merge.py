import pandas as pd

# Loads all files 2015-19
df2015 = pd.read_csv("2015.csv")
df2016 = pd.read_csv("2016.csv")
df2017 = pd.read_csv("2017.csv")
df2018 = pd.read_csv("2018.csv")
df2019 = pd.read_csv("2019.csv")

#Standardising columns
df2015 = df2015.rename(columns={
    "Country": "Country",
    "Happiness Score": "Happiness_Score",
    "Economy (GDP per Capita)": "GDP",
    "Family": "Social_Support",
    "Health (Life Expectancy)": "Life_Expectancy",
    "Freedom": "Freedom",
    "Trust (Government Corruption)": "Corruption",
    "Generosity": "Generosity"
})

df2016 = df2016.rename(columns={
    "Country": "Country",
    "Happiness Score": "Happiness_Score",
    "Economy (GDP per Capita)": "GDP",
    "Family": "Social_Support",
    "Health (Life Expectancy)": "Life_Expectancy",
    "Freedom": "Freedom",
    "Trust (Government Corruption)": "Corruption",
    "Generosity": "Generosity"
})

df2017 = df2017.rename(columns={
    "Country": "Country",
    "Happiness.Score": "Happiness_Score",
    "Economy..GDP.per.Capita.": "GDP",
    "Family": "Social_Support",
    "Health..Life.Expectancy.": "Life_Expectancy",
    "Freedom": "Freedom",
    "Trust..Government.Corruption.": "Corruption",
    "Generosity": "Generosity"
})

df2018 = df2018.rename(columns={
    "Country or region": "Country",
    "Score": "Happiness_Score",
    "GDP per capita": "GDP",
    "Social support": "Social_Support",
    "Healthy life expectancy": "Life_Expectancy",
    "Freedom to make life choices": "Freedom",
    "Perceptions of corruption": "Corruption",
    "Generosity": "Generosity"
})

df2019 = df2019.rename(columns={
    "Country or region": "Country",
    "Score": "Happiness_Score",
    "GDP per capita": "GDP",
    "Social support": "Social_Support",
    "Healthy life expectancy": "Life_Expectancy",
    "Freedom to make life choices": "Freedom",
    "Perceptions of corruption": "Corruption",
    "Generosity": "Generosity"
})

#Year columns added
keep_cols = ["Country","Happiness_Score","GDP","Social_Support",
             "Life_Expectancy","Freedom","Generosity","Corruption"]

dfs = []
for year, df in zip([2015,2016,2017,2018,2019],
                    [df2015,df2016,df2017,df2018,df2019]):
    df["Year"] = year
    dfs.append(df[keep_cols + ["Year"]])

#Merge and save
combined = pd.concat(dfs, ignore_index=True)
combined.to_csv("world_happiness_combined.csv", index=False)
print(combined.shape)   #Check total obs numbers
print(combined.isnull().sum())  #Count missing values