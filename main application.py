import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone, timedelta

# ==========================================
# UNIVERSAL APPLICATION CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="2026 World Cup Analytical Model",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# TOTAL SPORTS GRAPHICS BRANDING & THEME ENGINE
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&family=Bebas+Neue&display=swap');

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        background-color: #080B10 !important;
        color: #E2E8F0;
    }
    footer {visibility: hidden;}

    h1, h2, h3, h4, .stTabs [data-baseweb="tab-list"] button {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    h2 { color: #00FF87 !important; font-size: 2.2rem !important; }
    h3 { color: #F1F5F9 !important; }

    .pitch-banner {
        position: relative; text-align: center;
        padding: 48px 25px 38px 25px; border-radius: 14px;
        margin-bottom: 28px; overflow: hidden; border: 1px solid #1E293B;
        background:
            linear-gradient(180deg, rgba(8,11,16,0.55) 0%, rgba(8,11,16,0.94) 75%),
            repeating-linear-gradient(110deg, #123524 0px, #123524 70px, #0D2B1B 70px, #0D2B1B 140px);
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.6);
    }
    .kickoff-badge {
        display: inline-block; background-color: #00FF87; color: #04140C;
        font-family: 'Bebas Neue', sans-serif; font-size: 0.95rem;
        letter-spacing: 4px; padding: 6px 18px; border-radius: 999px; margin-bottom: 18px;
    }
    .hero-title {
        font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 3.4rem;
        color: #FFFFFF; text-transform: uppercase; letter-spacing: 2px; margin: 0;
        text-shadow: 0 0 25px rgba(0, 255, 135, 0.35);
    }
    .hero-subtitle {
        font-family: 'Oswald', sans-serif; color: #00FF87; font-size: 1.5rem;
        letter-spacing: 4px; margin: 8px 0 16px 0;
    }
    .hero-tagline {
        max-width: 760px; margin: 0 auto 18px auto;
        color: #94A3B8; font-size: 1rem; line-height: 1.6;
    }
    .host-flags { font-family: 'Oswald', sans-serif; font-size: 1rem; letter-spacing: 2px; color: #E2E8F0; }

    .stTabs [data-baseweb="tab-list"] {
        background-color: #111622; border-radius: 8px; padding: 6px; border: 1px solid #1E293B;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.2rem !important; color: #94A3B8 !important; padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #00FF87 !important; color: #000000 !important;
        font-weight: 700; border-radius: 6px;
    }

    .streamlit-expanderHeader {
        background-color: #111622 !important; border: 1px solid #1E293B !important;
        font-family: 'Oswald', sans-serif; font-size: 1.4rem !important;
        color: #FFFFFF !important; border-radius: 6px !important;
    }

    [data-testid="stMetric"] {
        background-color: #111622; border: 1px solid #1E293B;
        border-left: 4px solid #00FF87; border-radius: 10px; padding: 14px 16px;
    }
    [data-testid="stMetricValue"] {
        font-family: 'Bebas Neue', 'Oswald', sans-serif;
        font-size: 2.3rem !important; color: #00FF87 !important; letter-spacing: 1px;
    }
    [data-testid="stMetricLabel"] {
        font-family: 'Space Grotesk', sans-serif; text-transform: uppercase;
        font-size: 0.8rem !important; color: #94A3B8 !important; letter-spacing: 1.5px;
    }

    section[data-testid="stSidebar"] {
        background-color: #0D121F; border-right: 1px solid #1E293B;
    }
    section[data-testid="stSidebar"] * { color: #E2E8F0 !important; }
    section[data-testid="stSidebar"] h3 { color: #00FF87 !important; }

    .team-banner {
        display: flex; justify-content: space-between; align-items: center;
        flex-wrap: wrap; gap: 10px; padding: 18px 26px; border-radius: 10px;
        margin-bottom: 20px; box-shadow: 0 10px 25px -8px rgba(0, 0, 0, 0.6);
    }
    .team-banner-name { font-family: 'Oswald', sans-serif; font-size: 2rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .team-banner-tag { font-family: 'Bebas Neue', sans-serif; font-size: 1.1rem; letter-spacing: 4px; opacity: 0.75; }

    .team-argentine { background-color: #1D4ED8 !important; color: #FFFFFF !important; border-left: 5px solid #60A5FA; }
    .team-brazil    { background-color: #15803D !important; color: #FDE047 !important; border-left: 5px solid #EAB308; }
    .team-spain     { background-color: #991B1B !important; color: #FDE047 !important; border-left: 5px solid #F59E0B; }
    .team-england   { background-color: #F8FAFC !important; color: #0F172A !important; border-left: 5px solid #E2E8F0; }
    .team-france    { background-color: #1E3A8A !important; color: #FFFFFF !important; border-left: 5px solid #3B82F6; }
    .team-netherlands { background-color: #C2410C !important; color: #FFFFFF !important; border-left: 5px solid #F97316; }
    .team-mexico    { background-color: #065F46 !important; color: #FFFFFF !important; border-left: 5px solid #10B981; }
    .team-ecuador   { background-color: #B45309 !important; color: #FDE047 !important; border-left: 5px solid #F59E0B; }
    .team-germany   { background-color: #1A1A1A !important; color: #FFCE00 !important; border-left: 5px solid #DD0000; }
    .team-colombia  { background-color: #003893 !important; color: #FFCD00 !important; border-left: 5px solid #C8102E; }
    .team-portugal  { background-color: #006633 !important; color: #FFFFFF !important; border-left: 5px solid #FF0000; }
    .team-uruguay   { background-color: #0F3460 !important; color: #75AADB !important; border-left: 5px solid #75AADB; }
    .team-croatia   { background-color: #DC2626 !important; color: #FFFFFF !important; border-left: 5px solid #FFFFFF; }
    .team-japan     { background-color: #1E1E1E !important; color: #FFFFFF !important; border-left: 5px solid #BC002D; }
    .team-senegal   { background-color: #00853F !important; color: #FDEF42 !important; border-left: 5px solid #E31B23; }
    .team-norway    { background-color: #BA0C2F !important; color: #FFFFFF !important; border-left: 5px solid #00205B; }
    .team-paraguay  { background-color: #D52B1E !important; color: #FFFFFF !important; border-left: 5px solid #0038A8; }

    .stMarkdown table {
        width: 100%; border-collapse: collapse; background-color: #111622;
        border-radius: 8px; overflow: hidden; font-size: 0.95rem;
    }
    .stMarkdown table thead th {
        background-color: #00FF87; color: #04140C; font-family: 'Oswald', sans-serif;
        text-transform: uppercase; letter-spacing: 1px; padding: 10px 14px; text-align: left;
    }
    .stMarkdown table td { padding: 9px 14px; border-bottom: 1px solid #1E293B; color: #E2E8F0; }
    .stMarkdown table tbody tr:nth-child(even) td { background-color: #161D30; }
    .stMarkdown table tbody tr:hover td { background-color: #1E293B; }

    .grand-champion-platform {
        background: linear-gradient(135deg, #FEF08A 0%, #CA8A04 100%); color: #000000;
        text-align: center; padding: 28px 15px; border-radius: 10px;
        font-family: 'Oswald', sans-serif; font-size: 2.6rem; font-weight: 700;
        box-shadow: 0 0 30px rgba(234, 179, 8, 0.4); border: 2px solid #FAC827;
        letter-spacing: 1.5px; text-transform: uppercase;
    }
    .champ-subtext {
        font-family: 'Space Grotesk', sans-serif; font-size: 0.9rem; font-weight: 700;
        color: #713F12; margin-top: 8px; letter-spacing: 1px; text-transform: uppercase;
    }

    /* ==========================================
       FIXTURE CALENDAR TAB STYLES
    ========================================== */
    .fx-day-anchor { scroll-margin-top: 80px; }

    .fx-date-header {
        display: flex; align-items: center; gap: 14px;
        padding: 14px 0 10px 0; margin-top: 10px;
    }
    .fx-date-pill {
        font-family: 'Oswald', sans-serif; font-size: 1.05rem; font-weight: 700;
        letter-spacing: 1.5px; text-transform: uppercase;
        padding: 6px 18px; border-radius: 999px;
        background-color: #1E293B; color: #94A3B8; border: 1px solid #334155;
        white-space: nowrap;
    }
    .fx-date-pill.today {
        background-color: #00FF87; color: #04140C;
        border-color: #00FF87; box-shadow: 0 0 14px rgba(0,255,135,0.35);
    }
    .fx-date-pill.past { background-color: #111622; color: #475569; border-color: #1E293B; }
    .fx-date-line { flex: 1; height: 1px; background: #1E293B; }

    .fx-card {
        background-color: #111622; border: 1px solid #1E293B;
        border-radius: 10px; padding: 14px 18px; margin-bottom: 10px;
        display: flex; align-items: center; gap: 14px;
        transition: border-color 0.2s;
    }
    .fx-card:hover { border-color: #334155; }
    .fx-card.today-match { border-color: #00FF87 !important; box-shadow: 0 0 12px rgba(0,255,135,0.12); }
    .fx-card.past-match  { opacity: 0.65; }

    .fx-match-num {
        font-family: 'Bebas Neue', sans-serif; font-size: 0.85rem;
        color: #475569; letter-spacing: 1px; min-width: 52px; text-align: center;
    }
    .fx-time-col {
        min-width: 68px; text-align: center;
    }
    .fx-time {
        font-family: 'Oswald', sans-serif; font-size: 1.15rem;
        font-weight: 700; color: #00FF87; letter-spacing: 1px;
    }
    .fx-ist-label {
        font-family: 'Space Grotesk', sans-serif; font-size: 0.65rem;
        color: #475569; letter-spacing: 1px; text-transform: uppercase;
    }
    .fx-teams {
        flex: 1; display: flex; align-items: center; gap: 10px;
        font-family: 'Oswald', sans-serif; font-size: 1.15rem;
        font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
    }
    .fx-home { color: #E2E8F0; text-align: right; flex: 1; }
    .fx-away { color: #E2E8F0; text-align: left; flex: 1; }
    .fx-vs   { color: #475569; font-size: 0.9rem; letter-spacing: 2px; flex-shrink: 0; }
    .fx-badge {
        font-family: 'Space Grotesk', sans-serif; font-size: 0.72rem; font-weight: 700;
        letter-spacing: 1.5px; text-transform: uppercase;
        padding: 3px 10px; border-radius: 999px; white-space: nowrap;
    }
    .badge-group  { background-color: #1E293B; color: #64748B; border: 1px solid #334155; }
    .badge-r32    { background-color: #1a2744; color: #6B9FFF; border: 1px solid #2d4a8a; }
    .badge-r16    { background-color: #1a3030; color: #4ECDC4; border: 1px solid #2d6060; }
    .badge-qf     { background-color: #2a1a44; color: #C084FC; border: 1px solid #5b3a8a; }
    .badge-sf     { background-color: #3a2200; color: #FB923C; border: 1px solid #8a5000; }
    .badge-3rd    { background-color: #1a2a1a; color: #86EFAC; border: 1px solid #2d6a2d; }
    .badge-final  { background-color: #3a2e00; color: #FDE047; border: 1px solid #8a7000; }
    .fx-stage-label {
        font-family: 'Space Grotesk', sans-serif; font-size: 0.7rem;
        color: #475569; min-width: 52px; text-align: right;
    }

    .fx-today-banner {
        background: linear-gradient(90deg, rgba(0,255,135,0.10) 0%, rgba(0,255,135,0.04) 100%);
        border: 1px solid rgba(0,255,135,0.25); border-radius: 10px;
        padding: 12px 20px; margin-bottom: 18px; text-align: center;
        font-family: 'Oswald', sans-serif; font-size: 1.1rem; color: #00FF87;
        letter-spacing: 2px; text-transform: uppercase;
    }

    .fx-scroll-info {
        background-color: #111622; border: 1px solid #1E293B;
        border-radius: 8px; padding: 10px 16px; margin-bottom: 18px;
        font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; color: #64748B;
        text-align: center; letter-spacing: 0.3px;
    }

    .app-footer {
        text-align: center; margin-top: 50px;
        padding: 24px 10px 18px 10px; border-top: 2px solid #1E293B;
        font-family: 'Space Grotesk', sans-serif;
    }
    .footer-line { color: #64748B; font-size: 0.85rem; margin-bottom: 6px; letter-spacing: 0.5px; }
    .footer-copyright { color: #475569; font-size: 0.85rem; letter-spacing: 0.5px; }
    .footer-copyright .highlight { color: #00FF87; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# FIXTURE DATA  (parsed from matches.csv + teams.csv)
# ==========================================
TEAM_NAMES = {
    1:"Mexico", 2:"South Africa", 3:"Korea Republic", 4:"Czechia",
    5:"Canada", 6:"Bosnia-Herzegovina", 7:"Qatar", 8:"Switzerland",
    9:"Brazil", 10:"Morocco", 11:"Haiti", 12:"Scotland",
    13:"United States", 14:"Paraguay", 15:"Australia", 16:"Türkiye",
    17:"Germany", 18:"Curaçao", 19:"Côte d'Ivoire", 20:"Ecuador",
    21:"Netherlands", 22:"Japan", 23:"Sweden", 24:"Tunisia",
    25:"Belgium", 26:"Egypt", 27:"IR Iran", 28:"New Zealand",
    29:"Spain", 30:"Cape Verde", 31:"Saudi Arabia", 32:"Uruguay",
    33:"France", 34:"Senegal", 35:"Iraq", 36:"Norway",
    37:"Argentina", 38:"Algeria", 39:"Austria", 40:"Jordan",
    41:"Portugal", 42:"Congo DR", 43:"Uzbekistan", 44:"Colombia",
    45:"England", 46:"Croatia", 47:"Ghana", 48:"Panama",
}

STAGE_NAMES = {1:"Group Stage", 2:"Round of 32", 3:"Round of 16", 4:"Quarterfinal", 5:"Semifinal", 6:"3rd Place", 7:"Final"}
STAGE_BADGE = {1:"badge-group", 2:"badge-r32", 3:"badge-r16", 4:"badge-qf", 5:"badge-sf", 6:"badge-3rd", 7:"badge-final"}
STAGE_LABEL = {1:"GROUP", 2:"R32", 3:"R16", 4:"QF", 5:"SF", 6:"3RD", 7:"FINAL"}

# Raw match rows: (match_number, home_id, away_id, stage_id, kickoff_utc_offset_str, match_label)
# kickoff_utc_offset_str format: "YYYY-MM-DD HH:MM:SS±HH"
_RAW = [
    (1, 1, 2, 1, "2026-06-11 19:00:00+00", "Group A"),
    (2, 3, 4, 1, "2026-06-12 02:00:00+00", "Group A"),
    (3, 5, 6, 1, "2026-06-12 19:00:00+00", "Group B"),
    (4, 13, 14, 1, "2026-06-13 01:00:00+00", "Group C"),
    (5, 7, 8, 1, "2026-06-13 19:00:00+00", "Group B"),
    (6, 9, 10, 1, "2026-06-13 22:00:00+00", "Group D"),
    (7, 11, 12, 1, "2026-06-14 01:00:00+00", "Group D"),
    (8, 15, 16, 1, "2026-06-14 04:00:00+00", "Group C"),
    (9, 17, 18, 1, "2026-06-14 17:00:00+00", "Group E"),
    (10, 21, 22, 1, "2026-06-14 20:00:00+00", "Group F"),
    (11, 19, 20, 1, "2026-06-14 23:00:00+00", "Group E"),
    (12, 23, 24, 1, "2026-06-15 02:00:00+00", "Group F"),
    (13, 29, 30, 1, "2026-06-15 16:00:00+00", "Group H"),
    (14, 25, 26, 1, "2026-06-15 19:00:00+00", "Group G"),
    (15, 31, 32, 1, "2026-06-15 22:00:00+00", "Group H"),
    (16, 27, 28, 1, "2026-06-16 01:00:00+00", "Group G"),
    (17, 33, 34, 1, "2026-06-16 19:00:00+00", "Group I"),
    (18, 35, 36, 1, "2026-06-16 22:00:00+00", "Group I"),
    (19, 37, 38, 1, "2026-06-17 01:00:00+00", "Group J"),
    (20, 39, 40, 1, "2026-06-17 04:00:00+00", "Group J"),
    (21, 41, 42, 1, "2026-06-17 17:00:00+00", "Group K"),
    (22, 45, 46, 1, "2026-06-17 20:00:00+00", "Group L"),
    (23, 47, 48, 1, "2026-06-17 23:00:00+00", "Group L"),
    (24, 43, 44, 1, "2026-06-18 02:00:00+00", "Group K"),
    (25, 4, 2, 1, "2026-06-18 16:00:00+00", "Group A"),
    (26, 8, 6, 1, "2026-06-18 19:00:00+00", "Group B"),
    (27, 5, 7, 1, "2026-06-18 22:00:00+00", "Group B"),
    (28, 1, 3, 1, "2026-06-19 01:00:00+00", "Group A"),
    (29, 13, 15, 1, "2026-06-19 19:00:00+00", "Group C"),
    (30, 12, 10, 1, "2026-06-19 22:00:00+00", "Group D"),
    (31, 9, 11, 1, "2026-06-20 00:30:00+00", "Group D"),
    (32, 16, 14, 1, "2026-06-20 04:00:00+00", "Group C"),
    (33, 21, 23, 1, "2026-06-20 17:00:00+00", "Group F"),
    (34, 17, 19, 1, "2026-06-20 20:00:00+00", "Group E"),
    (35, 20, 18, 1, "2026-06-21 00:00:00+00", "Group E"),
    (36, 24, 22, 1, "2026-06-21 04:00:00+00", "Group F"),
    (37, 29, 31, 1, "2026-06-21 16:00:00+00", "Group H"),
    (38, 25, 27, 1, "2026-06-21 19:00:00+00", "Group G"),
    (39, 32, 30, 1, "2026-06-21 22:00:00+00", "Group H"),
    (40, 28, 26, 1, "2026-06-22 01:00:00+00", "Group G"),
    (41, 37, 39, 1, "2026-06-22 17:00:00+00", "Group J"),
    (42, 33, 35, 1, "2026-06-22 21:00:00+00", "Group I"),
    (43, 36, 34, 1, "2026-06-23 00:00:00+00", "Group I"),
    (44, 40, 38, 1, "2026-06-23 03:00:00+00", "Group J"),
    (45, 41, 43, 1, "2026-06-23 17:00:00+00", "Group K"),
    (46, 45, 47, 1, "2026-06-23 20:00:00+00", "Group L"),
    (47, 48, 46, 1, "2026-06-23 23:00:00+00", "Group L"),
    (48, 44, 42, 1, "2026-06-24 02:00:00+00", "Group K"),
    (49, 8, 5, 1, "2026-06-24 19:00:00+00", "Group B"),
    (50, 6, 7, 1, "2026-06-24 19:00:00+00", "Group B"),
    (51, 12, 9, 1, "2026-06-24 22:00:00+00", "Group D"),
    (52, 10, 11, 1, "2026-06-24 22:00:00+00", "Group D"),
    (53, 4, 1, 1, "2026-06-25 01:00:00+00", "Group A"),
    (54, 2, 3, 1, "2026-06-25 01:00:00+00", "Group A"),
    (55, 18, 19, 1, "2026-06-25 20:00:00+00", "Group E"),
    (56, 20, 17, 1, "2026-06-25 20:00:00+00", "Group E"),
    (57, 22, 23, 1, "2026-06-25 23:00:00+00", "Group F"),
    (58, 24, 21, 1, "2026-06-25 23:00:00+00", "Group F"),
    (59, 16, 13, 1, "2026-06-26 02:00:00+00", "Group C"),
    (60, 14, 15, 1, "2026-06-26 02:00:00+00", "Group C"),
    (61, 36, 33, 1, "2026-06-26 19:00:00+00", "Group I"),
    (62, 34, 35, 1, "2026-06-26 19:00:00+00", "Group I"),
    (63, 30, 31, 1, "2026-06-27 00:00:00+00", "Group H"),
    (64, 32, 29, 1, "2026-06-27 00:00:00+00", "Group H"),
    (65, 26, 27, 1, "2026-06-27 03:00:00+00", "Group G"),
    (66, 28, 25, 1, "2026-06-27 03:00:00+00", "Group G"),
    (67, 48, 45, 1, "2026-06-27 21:00:00+00", "Group L"),
    (68, 46, 47, 1, "2026-06-27 21:00:00+00", "Group L"),
    (69, 44, 41, 1, "2026-06-27 23:30:00+00", "Group K"),
    (70, 42, 43, 1, "2026-06-27 23:30:00+00", "Group K"),
    (71, 38, 39, 1, "2026-06-28 02:00:00+00", "Group J"),
    (72, 40, 37, 1, "2026-06-28 02:00:00+00", "Group J"),
    (73, None, None, 2, "2026-06-28 22:00:00+00", "2A vs 2B"),
    (74, None, None, 2, "2026-06-29 18:00:00+00", "1C vs 2F"),
    (75, None, None, 2, "2026-06-29 20:30:00+00", "1E vs 3ABCDF"),
    (76, None, None, 2, "2026-06-30 03:00:00+00", "1F vs 2C"),
    (77, None, None, 2, "2026-06-30 18:00:00+00", "2E vs 2I"),
    (78, None, None, 2, "2026-06-30 21:00:00+00", "1I vs 3CDFGH"),
    (79, None, None, 2, "2026-07-01 03:00:00+00", "1A vs 3CEFHI"),
    (80, None, None, 2, "2026-07-01 16:00:00+00", "1L vs 3EHIJK"),
    (81, None, None, 2, "2026-07-01 23:00:00+00", "1G vs 3AEHIJ"),
    (82, None, None, 2, "2026-07-02 03:00:00+00", "1D vs 3BEFIJ"),
    (83, None, None, 2, "2026-07-02 22:00:00+00", "1H vs 2J"),
    (84, None, None, 2, "2026-07-02 23:00:00+00", "2K vs 2L"),
    (85, None, None, 2, "2026-07-03 06:00:00+00", "1B vs 3EFGIJ"),
    (86, None, None, 2, "2026-07-03 19:00:00+00", "2D vs 2G"),
    (87, None, None, 2, "2026-07-03 22:00:00+00", "1J vs 2H"),
    (88, None, None, 2, "2026-07-04 02:30:00+00", "1K vs 3DEIJL"),
    (89, None, None, 3, "2026-07-04 18:00:00+00", "W73 vs W75"),
    (90, None, None, 3, "2026-07-04 21:00:00+00", "W74 vs W77"),
    (91, None, None, 3, "2026-07-05 20:00:00+00", "W76 vs W78"),
    (92, None, None, 3, "2026-07-06 02:00:00+00", "W79 vs W80"),
    (93, None, None, 3, "2026-07-06 20:00:00+00", "W83 vs W84"),
    (94, None, None, 3, "2026-07-07 03:00:00+00", "W81 vs W82"),
    (95, None, None, 3, "2026-07-07 16:00:00+00", "W86 vs W88"),
    (96, None, None, 3, "2026-07-07 23:00:00+00", "W85 vs W87"),
    (97, None, None, 4, "2026-07-09 20:00:00+00", "W89 vs W90"),
    (98, None, None, 4, "2026-07-10 22:00:00+00", "W93 vs W94"),
    (99, None, None, 4, "2026-07-11 21:00:00+00", "W91 vs W92"),
    (100,None, None, 4, "2026-07-12 02:00:00+00", "W95 vs W100"),
    (101,None, None, 5, "2026-07-14 20:00:00+00", "W97 vs W98"),
    (102,None, None, 5, "2026-07-15 19:00:00+00", "W99 vs W100"),
    (103,None, None, 6, "2026-07-18 21:00:00+00", "RU101 vs RU102"),
    (104,None, None, 7, "2026-07-19 19:00:00+00", "W101 vs W102"),
]

IST = timezone(timedelta(hours=5, minutes=30))

def parse_kickoff_ist(s):
    """Parse '2026-06-11 15:00:00-06' to IST datetime."""
    dt_part, tz_part = s.rsplit("-" if s.count("-") == 3 else "+", 1) if "+" in s else (s[:-3], s[-3:])
    for i in range(len(s)-1, 9, -1):
        if s[i] in ("+", "-"):
            tz_sign = 1 if s[i] == "+" else -1
            tz_hours = int(s[i+1:])
            naive = datetime.strptime(s[:i], "%Y-%m-%d %H:%M:%S")
            utc_dt = naive - timedelta(hours=tz_sign * tz_hours)
            utc_dt = utc_dt.replace(tzinfo=timezone.utc)
            return utc_dt.astimezone(IST)
    raise ValueError(f"Cannot parse: {s}")

def build_fixtures():
    out = []
    for row in _RAW:
        mnum, hid, aid, stage_id, ko_str, label = row
        ko_ist = parse_kickoff_ist(ko_str)
        home = TEAM_NAMES.get(hid, "") if hid else ""
        away = TEAM_NAMES.get(aid, "") if aid else ""
        out.append({
            "match_num": mnum,
            "home": home,
            "away": away,
            "stage_id": stage_id,
            "label": label,
            "ko_ist": ko_ist,
            "date_ist": ko_ist.date(),
        })
    out.sort(key=lambda x: x["ko_ist"])
    return out

FIXTURES = build_fixtures()

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### Match Center")
    st.markdown("---")
    st.markdown("**Tournament:** 2026 FIFA World Cup")
    st.markdown("**Hosts:** USA &middot; Mexico &middot; Canada")
    st.markdown("**Field Size:** 48 Nations")
    st.markdown("---")
    st.markdown("#### Navigation Guide")
    st.markdown("- **The AI Engine** &mdash; methodology & model internals")
    st.markdown("- **Team Journeys** &mdash; squad-by-squad scouting reports")
    st.markdown("- **Fixtures (IST)** &mdash; full match schedule in India time")
    st.markdown("- **The Alpha Bracket** &mdash; full knockout projection")
    st.markdown("---")
    st.caption("Model outputs are probabilistic projections, not guarantees. Football is a game of fine margins.")

# ==========================================
# HERO BANNER
# ==========================================
st.markdown("""
    <div class="pitch-banner">
        <div class="kickoff-badge">LIVE PREDICTIVE MODEL</div>
        <div class="hero-title">2026 FIFA World Cup</div>
        <div class="hero-subtitle">Predictive Analytics Engine</div>
        <p class="hero-tagline">Machine Learning Simulation Pipeline Mapping Roster Efficiency, Travel Exhaustion, and Micro-Climate Physics.</p>
        <div class="host-flags">USA &nbsp;&middot;&nbsp; MEX &nbsp;&middot;&nbsp; CAN &nbsp; &mdash; A NORTH AMERICAN SUMMER TOURNAMENT</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# TABS
# ==========================================
tab_engine, tab_journeys, tab_fixtures, tab_bracket = st.tabs([
    "The AI Engine",
    "Team Journeys",
    "Fixtures (IST)",
    "The Alpha Bracket"
])

# ==========================================
# TAB 1: METHODOLOGY
# ==========================================
with tab_engine:
    st.header("Algorithmic Methodology")
    st.write("This structural pipeline evaluates physical tournament factors, adjusting baseline Elo configurations using localized environmental variables to generate raw advancement vectors.")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    metric_col1.metric("Historical Matches Checked", "50,000+")
    metric_col2.metric("Monte Carlo Replications", "1,000")
    metric_col3.metric("Modeled Competitors", "48")
    metric_col4.metric("Environmental Array", "Active")

    st.write("")
    st.markdown("### Operational Feature Engineering")

    with st.expander("Physical Exhaustion Index", expanded=True):
        st.write("""
        **Mechanic:** Quantifies cross-continental aviation vectors and absolute recovery increments between matchdays.
        **Impact:** Teams crossing multiple time zones on compressed schedules face clear performance penalties in late-game expected goal calculations compared to stationary rivals.
        """)
    with st.expander("Micro-Climate & Altitude Array"):
        st.write("""
        **Mechanic:** Factors geographic stadium elevation profiles directly into player stamina depletion layers.
        **Impact:** Teams unaccustomed to playing at high elevations show decreased late-stage efficiency, while host squads receive localized adaptation multipliers.
        """)
    with st.expander("Opponent-Adjusted Momentum Metrics"):
        st.write("""
        **Mechanic:** Processes trailing historical score lines using exponentially decayed moving averages adjusted for opponent strength.
        **Impact:** High-margin scorelines against elite competitors yield top-tier ratings. Victories over lower-tier teams are discounted to prevent ranking inflation.
        """)

# ==========================================
# TAB 2: TEAM JOURNEYS
# ==========================================
with tab_journeys:
    st.header("Team Analytics & Performance Portfolios")
    st.write("Squad-by-squad scouting dossiers, generated from the model's probability and tactical-form layers.")

    team_registry = {
        "Spain":       {"win": "34.2%", "final": "48.2%", "form": "Elite positional dominance and sustained possession patterns.", "rivals": "Mexico, Argentina",
                        "story": "The Multiverse Frontrunner. Across randomized Monte Carlo simulations, Spain leads in total title wins. Their possession-heavy system limits defensive errors and exposure to low-probability counters, making them highly resilient against classic tournament upsets."},
        "Argentina":   {"win": "25.3%", "final": "48.2%", "form": "Top-tier conversion efficiency against low defensive blocks.", "rivals": "France, Spain, England",
                        "story": "The Consensus Core Choice. Argentina demonstrates a clear competitive edge in high-leverage fixtures against elite components. In the baseline deterministic timeline, they navigate a demanding knockout path by outperforming structural defensive expectations."},
        "England":     {"win": "21.7%", "final": "40.9%", "form": "Deep talent distribution with high physical resilience.", "rivals": "Ecuador, Netherlands, Argentina",
                        "story": "The Roster Depth Juggernaut. England benefits from high team valuation metrics and clean travel scheduling across early groups. The model identifies their deep rotation options as an asset, though their conversion efficiency numbers drop slightly in final simulations."},
        "Germany":     {"win": "0.1%",  "final": "0.4%",  "form": "Strong tactical core neutralized by high-risk bracket pathing.", "rivals": "Mexico, Spain",
                        "story": "The Bracket Trap Victim. Despite carrying strong baseline player metrics, Germany faces a severe geographic and scheduling disadvantage. A projected early knockout meeting with host nation Mexico requires playing at high altitude on short recovery rest. The model identifies this specific fixture as a high-probability bottleneck that limits their deeper tournament equity."},
        "France":      {"win": "8.4%",  "final": "19.5%", "form": "High-efficiency vertical transition attack.", "rivals": "United States, Argentina",
                        "story": "The Early Bracket Bottleneck. France's core projection suffers due to a projected early meeting with Argentina in the quarterfinals. This early matchup against top-tier opposition lowers their overall baseline probability of reaching the finals."},
        "Netherlands": {"win": "2.1%",  "final": "8.9%",  "form": "Organized defensive shape, efficient tactical foul tracking.", "rivals": "Brazil, England",
                        "story": "The Structural Disrupter. The Netherlands shows solid values within defensive performance metrics. The model positions them to take advantage of teams dealing with recent defensive inconsistencies, projecting a deep run past the quarterfinals."},
        "Colombia":    {"win": "1.6%",  "final": "3.8%",  "form": "Consistent unbeaten run in regional qualifying play.", "rivals": "Japan, Netherlands",
                        "story": "The Form Peak Contender. Colombia benefits from high momentum weights in the model's tracking layer. Their intense regional form suggests comfortable progress through initial groups before hitting organized European defensive structures."},
        "Brazil":      {"win": "1.3%",  "final": "7.4%",  "form": "Recent defensive inconsistencies in continental qualification.", "rivals": "Senegal, Netherlands",
                        "story": "The Vulnerable Giant. While possessing high overall squad talent, Brazil is penalized for soft defensive tracking data over their recent qualification cycles. The model projects clear risks when facing disciplined counter-attacking teams."},
        "Ecuador":     {"win": "1.1%",  "final": "3.9%",  "form": "High cardiovascular recovery values, altitude acclimation.", "rivals": "Korea Republic, Switzerland, England",
                        "story": "The Altitude Outlier. Ecuador's physical profiles are well-suited to the high-temperature, high-altitude venues of the North American summer tournament. They routinely outrun European teams on short rest cycles."},
        "Portugal":    {"win": "1.0%",  "final": "2.9%",  "form": "Slowing transition speeds across their central midfield.", "rivals": "Czechia, Spain",
                        "story": "The Stagnating Contingent. While holding strong legacy team metrics, Portugal faces challenges against younger squads built for fast transition play. The model identifies risks during long, demanding tournament stretches."},
        "Uruguay":     {"win": "0.6%",  "final": "3.4%",  "form": "High-intensity counter-pressing structure.", "rivals": "Croatia, England",
                        "story": "The High-Attrition Squad. Uruguay's aggressive pressing tactics yield early group-stage advantages but lead to noticeable fatigue accumulation across later rounds, reducing their depth value in long tournament simulations."},
        "Croatia":     {"win": "0.6%",  "final": "2.4%",  "form": "Experienced tactical spine with physical recovery limits.", "rivals": "Uruguay",
                        "story": "The Legacy Dynamic. Croatia retains an elite tactical core, but tracking models flag their older roster as vulnerable to younger, physical pressing teams during late knockout rounds."},
        "Japan":       {"win": "0.4%",  "final": "1.8%",  "form": "Sustained high-tempo pressing and rapid transition output.", "rivals": "Colombia",
                        "story": "The Tactical Giant Killer. Japan holds a clear track record of securing positive results against high-possession teams. Their disciplined defensive shape makes them a dangerous wildcard in knockout brackets."},
        "Senegal":     {"win": "0.3%",  "final": "1.3%",  "form": "Dominant physical and athletic core metrics.", "rivals": "Brazil",
                        "story": "The Athletic Wildcard. Senegal possesses the direct running power and physical profile needed to stress elite European backlines, though lower overall finishing metrics caps their final championship equity."},
        "Norway":      {"win": "0.3%",  "final": "2.1%",  "form": "Highly concentrated offensive production from key starters.", "rivals": "Scotland, Argentina",
                        "story": "The High-Variance Attack. Norway's core projections are driven by outlier attacking talent. Their efficient finishing data means they can occasionally outscore high-level opponents regardless of possession shares."},
        "Paraguay":    {"win": "0.2%",  "final": "0.5%",  "form": "Low-event defensive setup, low tactical risk.", "rivals": "Switzerland",
                        "story": "The Defensive Gridlock. Paraguay excels at slowing match tempos and limiting clear chances. While this keeps scorelines close, their lower scoring rates restrict their ability to mount deep comebacks."},
    }

    team_color_class = {
        "Spain":"team-spain","Argentina":"team-argentine","England":"team-england",
        "Germany":"team-germany","France":"team-france","Netherlands":"team-netherlands",
        "Colombia":"team-colombia","Brazil":"team-brazil","Ecuador":"team-ecuador",
        "Portugal":"team-portugal","Uruguay":"team-uruguay","Croatia":"team-croatia",
        "Japan":"team-japan","Senegal":"team-senegal","Norway":"team-norway","Paraguay":"team-paraguay"
    }

    selection = st.selectbox("Select Team Profile Archive:", list(team_registry.keys()))
    record = team_registry[selection]
    css_class = team_color_class.get(selection, "team-argentine")

    st.markdown(f"""
        <div class="team-banner {css_class}">
            <span class="team-banner-name">{selection}</span>
            <span class="team-banner-tag">SQUAD DOSSIER</span>
        </div>
    """, unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)
    col_v1.metric("Tournament Win Equity", record['win'])
    col_v2.metric("Reach Final Equity", record['final'])
    st.markdown(f"**Calculated Tactical Form:** {record['form']}")
    st.markdown(f"**Projected Bracket Paths:** {record['rivals']}")
    st.write("")
    st.info(f"{record['story']}")

# ==========================================
# TAB 3: FIXTURES IN IST
# ==========================================
with tab_fixtures:
    st.header("Full Match Schedule &mdash; India Standard Time (IST)")
    st.write("All 104 matches of the 2026 FIFA World Cup with exact kick-off times converted to IST (UTC +5:30).")

    now_ist = datetime.now(IST)
    today_ist = now_ist.date()

    all_dates = sorted(set(f["date_ist"] for f in FIXTURES))
    tourney_start = all_dates[0]
    tourney_end   = all_dates[-1]

    if today_ist < tourney_start:
        active_date = tourney_start
        date_label  = f"Tournament starts {tourney_start.strftime('%d %b %Y')} &mdash; showing first matchday"
    elif today_ist > tourney_end:
        active_date = tourney_end
        date_label  = f"Tournament concluded {tourney_end.strftime('%d %b %Y')} &mdash; showing final matchday"
    else:
        active_date = today_ist
        date_label  = f"Showing today's matches: {today_ist.strftime('%A, %d %B %Y')} (IST)"

    st.markdown(f"""
        <div class="fx-today-banner">
            {date_label}
        </div>
        <div class="fx-scroll-info">
            All times in <strong>IST (UTC +5:30)</strong> &middot;
            Scroll <strong>up</strong> for earlier matches &middot;
            Scroll <strong>down</strong> for upcoming fixtures
        </div>
    """, unsafe_allow_html=True)

    from collections import defaultdict
    by_date = defaultdict(list)
    for f in FIXTURES:
        by_date[f["date_ist"]].append(f)

    sorted_dates = sorted(by_date.keys())
    today_anchor_id = f"day-{active_date.isoformat()}"

    for d in sorted_dates:
        matches  = by_date[d]
        is_today = (d == active_date)
        is_past  = (d < active_date)

        if is_today:
            pill_class = "fx-date-pill today"
            label_txt  = f"TODAY &mdash; {d.strftime('%A, %d %B %Y')}"
        elif is_past:
            pill_class = "fx-date-pill past"
            label_txt  = d.strftime("%A, %d %B %Y")
        else:
            pill_class = "fx-date-pill"
            label_txt  = d.strftime("%A, %d %B %Y")

        anchor_id = f"day-{d.isoformat()}"
        day_html = f'<div class="fx-day-anchor" id="{anchor_id}"><div class="fx-date-header"><span class="{pill_class}">{label_txt}</span><div class="fx-date-line"></div></div></div>'

        for m in sorted(matches, key=lambda x: x["ko_ist"]):
            card_cls  = "fx-card today-match" if is_today else ("fx-card past-match" if is_past else "fx-card")
            time_str  = m["ko_ist"].strftime("%H:%M")
            badge_cls = STAGE_BADGE.get(m["stage_id"], "badge-group")
            stage_lbl = STAGE_LABEL.get(m["stage_id"], "")

            if m["home"] and m["away"]:
                home, away = m["home"], m["away"]
            else:
                parts = m["label"].split(" vs ")
                home = parts[0] if parts else "TBD"
                away = parts[1] if len(parts) > 1 else "TBD"

            day_html += (
                f'<div class="{card_cls}">'
                f'<div class="fx-match-num">Match {m["match_num"]}</div>'
                f'<div class="fx-time-col"><div class="fx-time">{time_str}</div><div class="fx-ist-label">IST</div></div>'
                f'<div class="fx-teams"><span class="fx-home">{home}</span><span class="fx-vs">VS</span><span class="fx-away">{away}</span></div>'
                f'<span class="fx-badge {badge_cls}">{stage_lbl}</span>'
                f'</div>'
            )

        st.markdown(day_html, unsafe_allow_html=True)

    # Securely inject a hidden iframe with a continuous state monitor.
    # It tracks the visibility of the tab and triggers a scroll EVERY time 
    # the user navigates back to the Fixtures tab.
    components.html(
        f"""
        <script>
            var parentDoc = window.parent.document;
            var targetId = '{today_anchor_id}';
            var wasVisible = false;

            setInterval(function() {{
                var el = parentDoc.getElementById(targetId);
                
                if (el) {{
                    /* Check if the element is currently visible on screen */
                    var isVisible = (el.offsetParent !== null);
                    
                    /* If it is visible NOW, but wasn't visible a moment ago, the user just clicked the tab */
                    if (isVisible && !wasVisible) {{
                        /* Add a tiny 100ms delay to let Streamlit's CSS tab transition finish before scrolling */
                        setTimeout(function() {{
                            el.scrollIntoView({{behavior: 'smooth', block: 'center'}});
                        }}, 100);
                    }}
                    
                    /* Update the state for the next check */
                    wasVisible = isVisible;
                }}
            }}, 250); /* Check the state every 250 milliseconds */
        </script>
        """,
        height=0,
        width=0,
    )

# ==========================================
# TAB 4: THE ALPHA BRACKET
# ==========================================
with tab_bracket:
    st.header("The Consensus Tournament Timeline")
    st.write("Deterministic progression matrix built entirely with native Streamlit data tables to ensure zero rendering errors and maximum readability.")
    st.write("---")

    GROUPS = {
        "Group A": ["Mexico", "South Africa", "Korea Republic", "Czechia"],
        "Group B": ["Canada", "Bosnia-Herzegovina", "Qatar", "Switzerland"],
        "Group C": ["United States", "Paraguay", "Australia", "Türkiye"],
        "Group D": ["Brazil", "Morocco", "Haiti", "Scotland"],
        "Group E": ["Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"],
        "Group F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
        "Group G": ["Belgium", "Egypt", "IR Iran", "New Zealand"],
        "Group H": ["Spain", "Cape Verde", "Saudi Arabia", "Uruguay"],
        "Group I": ["France", "Senegal", "Iraq", "Norway"],
        "Group J": ["Argentina", "Algeria", "Austria", "Jordan"],
        "Group K": ["Portugal", "Congo DR", "Uzbekistan", "Colombia"],
        "Group L": ["England", "Croatia", "Ghana", "Panama"],
    }

    GROUP_STAGE_MATCHES = [
        ("2026-06-11","Mexico","South Africa",2.28,0.63,2,1),
        ("2026-06-11","Korea Republic","Czechia",1.26,0.96,1,1),
        ("2026-06-12","Canada","Bosnia-Herzegovina",2.04,0.77,2,1),
        ("2026-06-12","United States","Paraguay",1.09,1.04,1,1),
        ("2026-06-13","Qatar","Switzerland",0.79,2.09,1,2),
        ("2026-06-13","Brazil","Morocco",1.87,0.78,2,1),
        ("2026-06-13","Haiti","Scotland",1.03,1.39,1,1),
        ("2026-06-13","Australia","Türkiye",2.17,0.79,2,1),
        ("2026-06-14","Germany","Curaçao",3.00,0.71,3,1),
        ("2026-06-14","Netherlands","Japan",1.61,0.82,2,1),
        ("2026-06-14","Côte d'Ivoire","Ecuador",1.10,1.85,1,2),
        ("2026-06-14","Sweden","Tunisia",1.90,0.83,2,1),
        ("2026-06-15","Belgium","Egypt",2.10,0.79,2,1),
        ("2026-06-15","Spain","Cape Verde",3.09,0.64,3,1),
        ("2026-06-15","IR Iran","New Zealand",1.67,0.75,2,1),
        ("2026-06-15","Saudi Arabia","Uruguay",0.85,1.59,1,2),
        ("2026-06-16","France","Senegal",1.96,0.83,2,1),
        ("2026-06-16","Iraq","Norway",0.97,1.70,1,2),
        ("2026-06-16","Argentina","Algeria",2.33,0.64,2,1),
        ("2026-06-16","Austria","Jordan",1.83,0.75,2,1),
        ("2026-06-17","Portugal","Congo DR",2.32,0.67,2,1),
        ("2026-06-17","England","Croatia",1.94,0.72,2,1),
        ("2026-06-17","Ghana","Panama",1.03,1.28,1,1),
        ("2026-06-17","Uzbekistan","Colombia",0.88,1.50,1,2),
        ("2026-06-18","Czechia","South Africa",2.21,0.84,2,1),
        ("2026-06-18","Switzerland","Bosnia-Herzegovina",2.14,0.58,2,1),
        ("2026-06-18","Canada","Qatar",1.97,0.51,2,1),
        ("2026-06-18","Mexico","Korea Republic",2.35,0.84,2,1),
        ("2026-06-19","United States","Australia",1.29,1.10,1,1),
        ("2026-06-19","Scotland","Morocco",1.30,0.99,1,1),
        ("2026-06-19","Türkiye","Paraguay",1.08,1.10,1,1),
        ("2026-06-19","Brazil","Haiti",2.94,0.65,3,1),
        ("2026-06-20","Netherlands","Sweden",2.25,0.50,2,0),
        ("2026-06-20","Germany","Côte d'Ivoire",2.12,0.66,2,1),
        ("2026-06-20","Ecuador","Curaçao",2.15,0.52,2,1),
        ("2026-06-20","Tunisia","Japan",0.97,1.66,1,2),
        ("2026-06-21","Spain","Saudi Arabia",3.03,0.65,3,1),
        ("2026-06-21","Belgium","IR Iran",2.23,0.75,2,1),
        ("2026-06-21","Uruguay","Cape Verde",2.34,0.66,2,1),
        ("2026-06-21","New Zealand","Egypt",1.30,1.00,1,1),
        ("2026-06-22","Argentina","Austria",2.26,0.66,2,1),
        ("2026-06-22","France","Iraq",2.95,0.65,3,1),
        ("2026-06-22","Norway","Senegal",1.60,0.86,2,1),
        ("2026-06-22","Jordan","Algeria",1.28,0.99,1,1),
        ("2026-06-23","Portugal","Uzbekistan",2.21,0.66,2,1),
        ("2026-06-23","England","Ghana",2.99,0.73,3,1),
        ("2026-06-23","Panama","Croatia",1.01,1.09,1,1),
        ("2026-06-23","Colombia","Congo DR",2.46,0.72,2,1),
        ("2026-06-24","Switzerland","Canada",1.73,1.01,2,1),
        ("2026-06-24","Bosnia-Herzegovina","Qatar",2.17,0.78,2,1),
        ("2026-06-24","Scotland","Brazil",1.28,1.28,1,1),
        ("2026-06-24","Morocco","Haiti",2.21,0.67,2,1),
        ("2026-06-24","South Africa","Korea Republic",1.21,1.05,1,1),
        ("2026-06-24","Czechia","Mexico",1.21,1.02,1,1),
        ("2026-06-25","Curaçao","Côte d'Ivoire",1.02,1.33,1,1),
        ("2026-06-25","Ecuador","Germany",1.90,0.86,2,1),
        ("2026-06-25","Japan","Sweden",1.96,0.72,2,1),
        ("2026-06-25","Tunisia","Netherlands",0.76,1.83,1,2),
        ("2026-06-25","Paraguay","Australia",1.60,0.83,2,1),
        ("2026-06-25","Türkiye","United States",1.69,0.98,2,1),
        ("2026-06-26","Norway","France",1.08,1.05,1,1),
        ("2026-06-26","Senegal","Iraq",2.13,0.65,2,1),
        ("2026-06-26","Uruguay","Spain",1.06,1.82,1,2),
        ("2026-06-26","Cape Verde","Saudi Arabia",1.45,0.92,1,1),
        ("2026-06-26","Egypt","IR Iran",1.59,0.90,2,1),
        ("2026-06-26","New Zealand","Belgium",0.90,1.79,1,2),
        ("2026-06-27","Panama","England",0.93,1.96,1,2),
        ("2026-06-27","Croatia","Ghana",2.95,0.65,3,1),
        ("2026-06-27","Colombia","Portugal",1.44,0.93,1,1),
        ("2026-06-27","Congo DR","Uzbekistan",1.30,1.08,1,1),
        ("2026-06-27","Jordan","Argentina",0.82,1.99,1,2),
        ("2026-06-27","Algeria","Austria",1.30,0.99,1,1),
    ]

    def compute_group_standings(group_name):
        teams = GROUPS[group_name]
        stats = {t: {"P":0,"W":0,"D":0,"L":0,"GF":0,"GA":0} for t in teams}
        for _, home, away, _, _, hs, as_ in GROUP_STAGE_MATCHES:
            if home in teams and away in teams:
                stats[home]["P"]+=1; stats[away]["P"]+=1
                stats[home]["GF"]+=hs; stats[home]["GA"]+=as_
                stats[away]["GF"]+=as_; stats[away]["GA"]+=hs
                if hs>as_:   stats[home]["W"]+=1; stats[away]["L"]+=1
                elif hs<as_: stats[away]["W"]+=1; stats[home]["L"]+=1
                else:        stats[home]["D"]+=1; stats[away]["D"]+=1
        rows=[]
        for t in teams:
            s=stats[t]; pts=s["W"]*3+s["D"]; gd=s["GF"]-s["GA"]
            rows.append({"team":t,"pts":pts,"gd":gd,**s})
        rows.sort(key=lambda r:(-r["pts"],-r["gd"],-r["GF"],r["team"]))
        return rows

    def render_group_standings(group_name):
        rows=compute_group_standings(group_name)
        qual={0:"[Q]",1:"[Q]",2:"[W]",3:"[E]"}
        lines=["| Pos | Team | P | W | D | L | GF | GA | GD | Pts |","| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"]
        for i,r in enumerate(rows):
            lines.append(f"| {qual[i]} {i+1} | **{r['team']}** | {r['P']} | {r['W']} | {r['D']} | {r['L']} | {r['GF']} | {r['GA']} | {r['gd']:+d} | **{r['pts']}** |")
        return "\n".join(lines)

    def render_group_fixtures(group_name):
        teams=GROUPS[group_name]
        lines=["| Date | Fixture | Score | xG (H - A) |","| :--- | :--- | :---: | :---: |"]
        for date,home,away,hxg,axg,hs,as_ in GROUP_STAGE_MATCHES:
            if home in teams and away in teams:
                lines.append(f"| {date} | {home} vs {away} | **{hs} - {as_}** | {hxg:.2f} - {axg:.2f} |")
        return "\n".join(lines)

    st.subheader("Group Stage")
    st.write("All 72 simulated Group Stage fixtures across the tournament's 12 groups, with final standings, results, and Expected Goals (xG) generated by the model.")
    st.caption("[Q] Direct knockout qualification &middot; [W] Best third-place contention &middot; [E] Eliminated")

    group_select = st.selectbox("Select Group:", list(GROUPS.keys()))
    col_standings, col_fixtures = st.columns([1, 1.3])
    with col_standings:
        st.markdown(f"##### {group_select} &mdash; Final Standings")
        st.markdown(render_group_standings(group_select))
    with col_fixtures:
        st.markdown(f"##### {group_select} &mdash; Fixtures & Results")
        st.markdown(render_group_fixtures(group_select))

    st.write("---")
    st.subheader("Round of 32 (16 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (96.1%)** | New Zealand (3.9%) | **Argentina** |
    | **England (91.4%)** | Algeria (8.6%) | **England** |
    | **Netherlands (83.3%)** | Bosnia-Herzegovina (16.7%) | **Netherlands** |
    | **Spain (89.4%)** | Austria (10.6%) | **Spain** |
    | **Mexico (80.5%)** | Cote d'Ivoire (19.5%) | **Mexico** |
    | **Brazil (86.9%)** | Senegal (13.1%) | **Brazil** |
    | **Ecuador (93.6%)** | Korea Republic (6.4%) | **Ecuador** |
    | **Canada (57.2%)** | Morocco (42.8%) | **Canada** |
    | **France (94.8%)** | United States (5.2%) | **France** |
    | **Switzerland (77.3%)** | Paraguay (22.7%) | **Switzerland** |
    | **Belgium (78.1%)** | Turkiye (21.9%) | **Belgium** |
    | **Germany (91.8%)** | IR Iran (8.2%) | **Germany** |
    | **Portugal (88.9%)** | Czechia (11.1%) | **Portugal** |
    | **Colombia (74.0%)** | Japan (26.0%) | **Colombia** |
    | **Uruguay (58.4%)** | Croatia (41.6%) | **Uruguay** |
    | **Norway (86.3%)** | Scotland (13.7%) | **Norway** |
    """)

    st.write("---")
    st.subheader("Round of 16 (8 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (87.2%)** | Norway (12.8%) | **Argentina** |
    | **England (81.4%)** | Uruguay (18.6%) | **England** |
    | **Netherlands (71.9%)** | Colombia (28.1%) | **Netherlands** |
    | **Spain (91.7%)** | Portugal (8.3%) | **Spain** |
    | **Mexico (80.3%)** | Germany (19.7%) | **Mexico** |
    | **Brazil (83.7%)** | Belgium (16.3%) | **Brazil** |
    | **Ecuador (79.7%)** | Switzerland (20.3%) | **Ecuador** |
    | **France (77.9%)** | Canada (22.1%) | **France** |
    """)

    st.write("---")
    st.subheader("Quarterfinals (4 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (76.6%)** | France (23.4%) | **Argentina** |
    | **Spain (95.8%)** | Mexico (4.2%) | **Spain** |
    | **England (76.3%)** | Ecuador (23.7%) | **England** |
    | **Netherlands (68.3%)** | Brazil (31.7%) | **Netherlands** |
    """)

    st.write("---")
    st.subheader("Semifinals (2 Matches)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (59.1%)** | Spain (40.9%) | **Argentina** |
    | **England (85.2%)** | Netherlands (14.8%) | **England** |
    """)

    st.write("---")
    st.subheader("The Final (1 Match)")
    st.markdown("""
    | Team A (Win Probability) | Team B (Win Probability) | Expected Winner |
    | :--- | :--- | :--- |
    | **Argentina (72.1%)** | England (27.9%) | **Argentina** |
    """)

    st.write("---")
    st.markdown("""
        <div class="grand-champion-platform">
            PREDICTED CHAMPION: ARGENTINA
            <div class="champ-subtext">2026 FIFA World Cup &mdash; Model Consensus Output</div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
    <div class="app-footer">
        <div class="footer-line">System Core Framework built using Python and XGBoost Ensembles.</div>
        <div class="footer-copyright">Copyright <span class="highlight">Soumyadeep Roy Chowdhury</span> 2026. All rights reserved.</div>
    </div>
""", unsafe_allow_html=True)