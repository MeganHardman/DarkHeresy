import streamlit as st
import pandas as pd
    
def load_df():
    df = pd.read_csv("./criticaldamage.csv")
    type_options = df.Type.unique()
    limb_options = df.Limb.unique()
    damage_options = df.Damage.unique()
    effect_options = df.Effect.unique()

    return df, type_options, limb_options, damage_options, effect_options

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

tab1, tab2, tab3 = st.tabs(["Damage", "Modifiers", "Additonal Info"])

with tab1:
    st.header("Critical Damage")
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
    
    cols = st.columns(3)
    type = cols[0].multiselect("Type", type_options)
    limb = cols[2].multiselect("Limb", limb_options)
    damage = cols[1].multiselect("Damage", damage_options)
    
    
    if effect_query != "":
        res = res.loc[res.Effect.str.contains(effect_query)]
    if type:
        res = check_rows("Type", type)
    if damage:
        res = check_rows("Damage", damage)
    if limb:
        res = check_rows("Limb", limb)

    st.write(res)

with tab2:
    if 'mod' not in st.session_state:
        st.session_state.mod = 0

    def Inc(inc_value=0):
        st.session_state.mod += inc_value
    
    def Dec(dec_value=0):
        st.session_state.mod -= dec_value
    
    
    st.header("Attack Modifiers")
    st.write(st.session_state.mod)
    st.checkbox("Short Range", value = False, key= 'short', help="+10", on_change = Inc, args=None, kwargs=dict(inc_value=10), disabled=False, label_visibility="visible")
    st.checkbox("Long Range", value = False, key= 'long', help="-10", on_change = Dec, args=None, kwargs=dict(dec_value=10), disabled=False, label_visibility="visible")
    st.checkbox("Cover", value = False, key= 'cover', help="-20", on_change = Dec, args=None, kwargs=dict(dec_value=20), disabled=False, label_visibility="visible")
    st.checkbox("Out numbered", value = False, key= 'out', help="+20", on_change = Inc, args=None, kwargs=dict(inc_value=10), disabled=False, label_visibility="visible")
    st.write("Hoard Size")
    st.checkbox("30 Mob (Massive)", value = False, key= 'mob', help="+30", on_change = Inc, args=None, kwargs=dict(inc_value=30), disabled=False, label_visibility="visible")
    st.checkbox("60 Throng (Immense)", value = False, key= 'throng', help="+40", on_change = Inc, args=None, kwargs=dict(inc_value=40), disabled=False, label_visibility="visible")
    st.checkbox("90 Assault (Monumental)", value = False, key= 'assault', help="+50", on_change = Inc, args=None, kwargs=dict(inc_value=50), disabled=False, label_visibility="visible")
    st.checkbox("120+ Tide (Titanic)", value = False, key= 'tide', help="+60", on_change = Inc, args=None, kwargs=dict(inc_value=60), disabled=False, label_visibility="visible")

with tab3:
    st.header("Info")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
