import streamlit as st
from services.cv_service import ask_cv

# Must be the first Streamlit command
st.set_page_config(
    page_title="Ali's AI Portfolio",
    page_icon=":material/work:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR HIGH-END UI (DARK MODE OPTIMIZED) ---
st.markdown(
    """
    <style>
    /* Import modern font & Material Symbols natively */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide ALL right-side header elements (Deploy, Share, GitHub, Menu) WITHOUT hiding the Sidebar Toggle */
    [data-testid="stActionPeers"] {display: none !important;}
    .stDeployButton {display: none !important;}
    #MainMenu {display: none !important;}
    
    /* Force hide the Streamlit Cloud "Viewer Badge" (Fork and GitHub buttons) */
    div[class^="viewerBadge_"] {display: none !important;}
    
    header {background: transparent !important;}
    footer {display: none !important;}
    
    /* Reduce massive default gaps in sidebar dividers */
    [data-testid="stSidebar"] hr {
        margin-top: 15px !important;
        margin-bottom: 15px !important;
    }

    /* Style the title (Vibrant Gradient for Dark/Light Mode) */
    .title-text {
        font-size: 2.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe, #00f2fe);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        line-height: 1.2;
        display: flex;
        align-items: center;
        gap: 12px;
        animation: shine 3s linear infinite;
    }
    
    @keyframes shine {
        to {
            background-position: 200% center;
        }
    }
    
    .title-icon {
        font-size: 2.8rem;
        -webkit-text-fill-color: #4facfe; /* Lock icon color to the gradient */
    }
    
    .subtitle-text {
        font-size: 1.1rem;
        color: #a0aec0; /* Beautiful soft grey for dark mode */
        # margin-top: 5px;
        # margin-bottom: 30px;
    }
    
    /* Clean up the sidebar buttons to adapt to dark/light natively */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        transition: all 0.3s;
        text-align: left;
        padding-left: 15px;
    }
    .stButton>button:hover {
        border-color: #4facfe;
        color: #4facfe;
        box-shadow: 0px 0px 10px rgba(79, 172, 254, 0.2);
    }
    
    /* Social Icons Layout styling */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .social-icons a {
        text-decoration: none;
        color: #a0aec0;
        transition: color 0.2s;
    }
    .social-icons a:hover {
        color: #4facfe;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR: Profile & Nav ---
with st.sidebar:
    import base64

    def get_base64_image(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except Exception:
            return ""

    profile_pic = get_base64_image("assets/mohib-profile.jpeg")
    img_src = (
        f"data:image/jpeg;base64,{profile_pic}"
        if profile_pic
        else "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    )

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center; margin-bottom: 5px;">
            <img src="{img_src}" width="120" height="120" style="object-fit: cover; border-radius: 50%; margin-bottom: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.2);">
            <h2 style="margin-top: 0px; margin-bottom: 5px; font-weight: 700;">Ali's AI Twin</h2>
            <span style="font-size: 0.95rem; color: #a0aec0; line-height: 1.4;">
                Welcome to my interactive portfolio! I've trained this AI on my <b>Resume</b>, <b>Projects</b>, and <b>Experience</b>.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("#### Suggested Questions")

    # State management for suggested questions
    if "suggested_question" not in st.session_state:
        st.session_state.suggested_question = None

    # Using native Material SVG icons for buttons
    if st.button("What are Ali's top skills?", icon=":material/psychology:"):
        st.session_state.suggested_question = (
            "What are your core technical skills and strengths?"
        )
    if st.button("Tell me about recent projects", icon=":material/work:"):
        st.session_state.suggested_question = (
            "Can you describe some of your recent professional projects?"
        )
    if st.button("Educational background?", icon=":material/school:"):
        st.session_state.suggested_question = (
            "Tell me about your educational background."
        )

    st.divider()

    # Social links using Real Brand SVGs (GitHub, LinkedIn, Gmail)
    st.markdown(
        """
        <div class="social-icons">
            <a href="mailto:alimohib025@gmail.com" target="_blank" title="Email Me">
                <svg viewBox="0 0 512 512" width="24" height="24" fill="currentColor">
                    <path d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48H48zM0 176V384c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V176L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"/>
                </svg>
            </a>
            <a href="https://github.com/CoderMohib" target="_blank" title="GitHub">
                <svg viewBox="0 0 496 512" width="24" height="24" fill="currentColor">
                    <path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/mohib-ali-80b19b294/" target="_blank" title="LinkedIn">
                <svg viewBox="0 0 448 512" width="24" height="24" fill="currentColor">
                    <path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/>
                </svg>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- MAIN CHAT UI ---
st.markdown(
    '<div class="title-text"><span class="material-symbols-rounded title-icon">smart_toy</span> Meet My AI Assistant</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle-text">Ask anything about my professional background, skills, and projects.</div>',
    unsafe_allow_html=True,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi there! I'm Ali's virtual assistant. I've analyzed his CV and experience. How can I help you today?",
        }
    ]

# Display chat messages from history
for message in st.session_state.messages:
    # Use built-in material icons for avatars so they flawlessly adapt to dark mode!
    avatar_icon = (
        ":material/person:" if message["role"] == "user" else ":material/smart_toy:"
    )
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.markdown(message["content"])

# React to user input or a suggested question click
user_input = st.chat_input("Type your message here...")

if st.session_state.suggested_question:
    user_input = st.session_state.suggested_question
    st.session_state.suggested_question = None

if user_input:
    # Display user message
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get assistant response
    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        with st.spinner("Analyzing Ali's Profile..."):
            response = ask_cv(user_input)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
