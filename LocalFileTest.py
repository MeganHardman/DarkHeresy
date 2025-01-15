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
    
    hl, number_options, roll_options, location_options = load_hl()
    hit = hl
    limb = ""
    
    my_comment = '''hit_query = st.number_input("Enter the hit roll")
    
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
            limb = "Leg"'''
    hit = hit.drop("Number", axis=1)
    column11, column12 = st.columns(2)
    with column11:
        st.subheader("Hit location Table")
        st.write(hit)
    with column12:
        st.subheader("Cover Table")
        st.write(
            pd.DataFrame(
                {
                    "Cover Type": ["Armour-glas, Thin Metal", "Flakboard,Storage Crate, Sandbags", "Statis Pod, Cogitator Bank", "Rockcrete, Hatchway, Thick iron, Stone", "Armaplas, Bulkhead, Plasteel"],
                    "Armour Points": [4, 8, 12, 16,32],
                }, index = False
            )
        )
        
    
    df, type_options, limb_options, damage_options, effect_options = load_df()
    res = df

    st.header("Critical Damage")
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
    #easy
    def EasyUnaware():
        if st.session_state.unaware:
            st.session_state.mod += 30
        else:
            st.session_state.mod -= 30
    def EasyPoint():
        if st.session_state.point:
            st.session_state.mod += 30
        else:
            st.session_state.mod -= 30
            
    #routine
    def RoutineOut():
        if st.session_state.outnumbered3:
            st.session_state.mod += 20
        else:
            st.session_state.mod -= 20
    def RoutineStunned():
        if st.session_state.stunned:
            st.session_state.mod += 20
        else:
            st.session_state.mod -= 20

    #Ordinary
    def OrdinaryShort():
        if st.session_state.short:
            st.session_state.mod += 10
        else:
            st.session_state.mod -= 10
    def OrdinaryOut():
        if st.session_state.outnumbered2:
            st.session_state.mod += 10
        else:
            st.session_state.mod -= 10
    def OrdinaryProne():
        if st.session_state.proneM:
            st.session_state.mod += 10
        else:
            st.session_state.mod -= 10
    def OrdinaryHigher():
        if st.session_state.higher:
            st.session_state.mod += 10
        else:
            st.session_state.mod -= 10

    #Difficult
    def DifficultLong():
        if st.session_state.long:
            st.session_state.mod -= 10
        else:
            st.session_state.mod += 10
    def DifficultProne():
        if st.session_state.proneS:
            st.session_state.mod -= 10
        else:
            st.session_state.mod += 10
    def DifficultTerrain():
        if st.session_state.terrain:
            st.session_state.mod -= 10
        else:
            st.session_state.mod += 10
    def DifficultFatigued():
        if st.session_state.fatigued:
            st.session_state.mod -= 10
        else:
            st.session_state.mod += 10

    #Hard
    def HardMelee():
        if st.session_state.melee:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def HardProne():
        if st.session_state.proneSelf:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def HardObscure():
        if st.session_state.obscure:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def HardDark():
        if st.session_state.darkM:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def HardUnarmed():
        if st.session_state.unarmed:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def HardTalent():
        if st.session_state.talent:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20

    #Very
    def VeryExtreme():
        if st.session_state.extreme:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    def VeryConcealed():
        if st.session_state.concealed:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    def VeryDark():
        if st.session_state.darkS:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    def VeryBrace():
        if st.session_state.brace:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    def VeryTerrain():
        if st.session_state.snow:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    
    #Enemy size
    def Emin():
        if st.session_state.mini:
            st.session_state.mod -= 30
        else:
            st.session_state.mod += 30
    def Epuny():
        if st.session_state.puny:
            st.session_state.mod -= 20
        else:
            st.session_state.mod += 20
    def Escrawn():
        if st.session_state.scrawny:
            st.session_state.mod -= 10
        else:
            st.session_state.mod += 10
    def Ehulk():
        if st.session_state.hulk:
            st.session_state.mod += 10
        else:
            st.session_state.mod -= 10
    def Een():
        if st.session_state.enormous:
            st.session_state.mod += 20
        else:
            st.session_state.mod -= 20
    def Emas():
        if st.session_state.massive:
            st.session_state.mod += 30
        else:
            st.session_state.mod -= 30
    def Eimm():
        if st.session_state.immense:
            st.session_state.mod += 40
        else:
            st.session_state.mod -= 40
    def Emon():
        if st.session_state.monumental:
            st.session_state.mod += 50
        else:
            st.session_state.mod -= 50
    def Etitan():
        if st.session_state.titanic:
            st.session_state.mod += 60
        else:
            st.session_state.mod -= 60

    
    #horde size
    def HM():
        if st.session_state.mob:
            st.session_state.mod += 30
        else:
            st.session_state.mod -= 30
    def HI():
        if st.session_state.throng:
            st.session_state.mod += 40
        else:
            st.session_state.mod -= 40
    def HA():
        if st.session_state.assault:
            st.session_state.mod += 50
        else:
            st.session_state.mod -= 50
    def HT():
        if st.session_state.tide:
            st.session_state.mod += 60
        else:
            st.session_state.mod -= 60
    
    st.header("Attack Modifiers")
    st.write(st.session_state.mod)

    c11,c12,c13 = st.columns(3, vertical_alignment="top")

    with c11:
        st.subheader("Easy +30")
        st.checkbox("Shooting at Surprised or Unaware foe", value = False, key= 'unaware', help="easy +30", on_change = EasyUnaware, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting at Point Blank Range", value = False, key= 'point', help="easy +30", on_change = EasyPoint, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.subheader("Difficult -10")
        st.checkbox("Shooting at Long Range", value = False, key= 'long', help=" -10", on_change = DifficultLong, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting at Prone foe", value = False, key= 'proneS', help=" -10", on_change = DifficultProne, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee in difficult terrain (mud, rain)", value = False, key= 'terrain', help="-10", on_change = DifficultTerrain, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Fatigued", value = False, key= 'fatigued', help=" -10", on_change = DifficultFatigued, args=None, kwargs=None, disabled=False, label_visibility="visible")
    
    with c12:
        st.subheader("Routine +20")
        st.checkbox("Melee against Outnumbered foes 3:1", value = False, key= 'outnumbered3', help="routine +20", on_change = RoutineOut, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting at Stunned foe", value = False, key= 'stunned', help="routine +20", on_change = RoutineStunned, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.subheader("Hard -20")
        st.checkbox("Shooting into Melee combat", value = False, key= 'melee', help="-20", on_change = HardMelee, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting while Prone", value = False, key= 'proneSelf', help="-20", on_change = HardProne, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting in Obscuring Conditions (fog, rain)", value = False, key= 'obscure', help="-20", on_change = HardObscure, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee in Darkness", value = False, key= 'darkM', help="-20", on_change = HardDark, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee Unarmed vs Armed foe", value = False, key= 'unarmed', help="-20", on_change = HardUnarmed, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Using a weapon without the right Talent", value = False, key= 'talent', help="-20", on_change = HardTalent, args=None, kwargs=None, disabled=False, label_visibility="visible")
    
    with c13:
        st.subheader("Ordinary +10")
        st.checkbox("Shooting at Short Range", value = False, key= 'short', help="ordinary +10", on_change = OrdinaryShort, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee against Outnumbered foes 2:1", value = False, key= 'outnumbered2', help="ordinary +10", on_change = OrdinaryOut, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee against Prone foe", value = False, key= 'proneM', help="ordinary +10", on_change = OrdinaryProne, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee from Higher Ground", value = False, key= 'higher', help="ordinary +10", on_change = OrdinaryHigher, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.subheader("Very Hard -30")
        st.checkbox("Shooting at Extreme Range", value = False, key= 'extreme', help="-30", on_change = VeryExtreme, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting at a Completely Concealed foe", value = False, key= 'concealed', help="-30", on_change = VeryConcealed, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting in Darkness", value = False, key= 'darkS', help="-30", on_change = VeryDark, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Shooting a Heavy Weapon without Bracing", value = False, key= 'brace', help="-30", on_change = VeryBrace, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Melee in very difficult terrain (deep snow)", value = False, key= 'snow', help="-30", on_change = VeryTerrain, args=None, kwargs=None, disabled=False, label_visibility="visible")

    c21, c22 = st.columns(2)

    with c21:
        st.subheader("Enemy Size")
        st.checkbox("Miniscule (autoquill, knife)", value = False, key= 'mini', help="-30", on_change = Emin, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Puny (bolt pistol,servo-skull)", value = False, key= 'puny', help="-20", on_change = Epuny, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Scrawny (Gretchin, Child)", value = False, key= 'scrawny', help="-10", on_change = Escrawn, args=None, kwargs=None, disabled=False, label_visibility="visible")
        #st.checkbox("Average (Human)", value = False, key= 'average', help="0", on_change = , args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Hulking (Ork Nob, Armoured Space Marine)", value = False, key= 'hulk', help="+10", on_change = Ehulk, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Enormous (Sentinel Walker,Krootox)", value = False, key= 'enormous', help="+20", on_change = Een, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Massive (Battle Tank, Greater Daemon)", value = False, key= 'massive', help="+30", on_change = Emas, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Immense (land Raider, Great Knarloc)", value = False, key= 'immense', help="+50", on_change = Eimm, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Monumental (Squiggoth, Baneblade)", value = False, key= 'monumental', help="+40", on_change = Emon, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("Titanic (Reaver Battle Titan)", value = False, key= 'titanic', help="+60", on_change = Etitan, args=None, kwargs=None, disabled=False, label_visibility="visible")

    with c22:
        st.subheader("Hoard Size")
        st.checkbox("30 Mob (Massive)", value = False, key= 'mob', help="+30", on_change = HM, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("60 Throng (Immense)", value = False, key= 'throng', help="+40", on_change = HI, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("90 Assault (Monumental)", value = False, key= 'assault', help="+50", on_change = HA, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.checkbox("120+ Tide (Titanic)", value = False, key= 'tide', help="+60", on_change = HT, args=None, kwargs=None, disabled=False, label_visibility="visible")

with tab3:
    st.header("Info")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
