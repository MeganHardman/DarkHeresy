import streamlit as st
import pandas as pd

# Cache our data
@st.cache()
def load_df():
    df = pd.read_csv("./criticaldamage.csv")
    type_options = df.Type.unique()
    damage_options = df.Damage.unique()
    effect_options = df.Effect.unique()


    #min_fare = df.Fare.min()
    #max_fare = df.Fare.max()

    #min_age = df.Age.min()
    #max_age = df.Age.max()

    return df, type_options, damage_options, effect_options#, embark_options, min_fare, max_fare, min_age, max_age

def check_rows(column, options):
    return res.loc[res[column].isin(options)]

st.title("Dark Heresy Critical Damage App")

df, type_options, damage_options, effect_options = load_df()
res = df

effect_query = st.text_input("String match for Effect")

cols = st.columns(3)
type = cols[0].multiselect("Type", type_options)
damage = cols[1].multiselect("Damage", damage_options)
#effect = cols[2].multiselect("Effect", effect_options)
#embark = cols[3].multiselect("Embarked", embark_options)

#range_cols = st.columns(3)
#min_fare_range, max_fare_range = range_cols[0].slider("Lowest Fare", float(min_fare), float(max_fare),
#                                        [float(min_fare), float(max_fare)])
#min_age_range, max_age_range = range_cols[2].slider("Lowest Age", float(min_age), float(max_age),
#                                        [float(min_age), float(max_age)])


if effect_query != "":
    res = res.loc[res.Effect.str.contains(effect_query)]

if type:
    res = check_rows("Type", type)
if damage:
    res = check_rows("Damage", damage)
#if effect:
#    res = check_rows("effect", effect)
#if embark:
#    res = check_rows("Embarked", embark)
#if range_cols[0].checkbox("Use Fare Range"):
#    res = res.loc[(res.Fare > min_fare_range) & (res.Age < max_fare_range)]
#if range_cols[2].checkbox("Use Age Range"):
#    res = res.loc[(res.Age > min_age_range) & (res.Age < max_age_range)]
#removal_columns = st.multiselect("Select Columns to Remove", df.columns.tolist())
#for column in removal_columns:
#    res = res.drop(column, axis=1)
#st.write(res)
