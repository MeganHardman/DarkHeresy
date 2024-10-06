import streamlit as st
import pandas as pd

# Cache our data
@st.cache()
def load_df():
    df = pd.read_csv("./criticaldamage.csv")
    type_options = df.Type.unique()
    limb_options = df.Limb.unique()
    damage_options = df.Damage.unique()
    effect_options = df.Effect.unique()


    #min_fare = df.Fare.min()
    #max_fare = df.Fare.max()

    #min_age = df.Age.min()
    #max_age = df.Age.max()

    return df, type_options, limb_options, damage_options, effect_options#, embark_options, min_fare, max_fare, min_age, max_age

def load_hl():
    hl = pd.read_csv("./hitlocations.csv")
    number_options = hl.Number.unique()
    roll_options = hl.Roll.unique()
    location_options = hl.Location.unique()

    return hl, number_options, roll_options, location_options

def check_rows(column, options):
    return res.loc[res[column].isin(options)]

def check_rows_limb(column, options):
    return hit.loc[hit[column].isin(options)]

st.title("Dark Heresy Critical Damage App")

hl, number_options, roll_options, location_options = load_hl()
hit = hl
limb = ""

hit_query = st.number_input("Enter the hit roll")

if hit_query :
    if hit_query < 11:
        hit = check_rows_limb("Number", 1)
        limb = "Head"
    elif hit_query < 21:
        hit = check_rows_limb("Number", 2)
        limb = "Arm"
    elif hit_query < 31:
        hit = check_rows_limb("Number", 3)
        limb = "Arm"
    elif hit_query < 71:
        hit = check_rows_limb("Number", 4)
        st.header("please help!")
        limb = "Body"
    elif hit_query < 85:
        hit = check_rows_limb("Number", 5)
        limb = "Leg"
    elif hit_query < 101:
        hit = check_rows_limb("Number", 6)
        limb = "Leg"
hit = hit.drop("Number", axis=1)
st.write(hit)

df, type_options, limb_options, damage_options, effect_options = load_df()
res = df

effect_query = st.text_input("String match for Effect")

cols = st.columns(4)
type = cols[0].multiselect("Type", type_options)
limb = cols[2].multiselect("Limb", limb_options)
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
if limb:
    res = check_rows("Limb", limb)
#if embark:
#    res = check_rows("Embarked", embark)
#if range_cols[0].checkbox("Use Fare Range"):
#    res = res.loc[(res.Fare > min_fare_range) & (res.Age < max_fare_range)]
#if range_cols[2].checkbox("Use Age Range"):
#    res = res.loc[(res.Age > min_age_range) & (res.Age < max_age_range)]
#removal_columns = st.multiselect("Select Columns to Remove", df.columns.tolist())
#for column in removal_columns:
#    res = res.drop(column, axis=1)
st.write(res)
