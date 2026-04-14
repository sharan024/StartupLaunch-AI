import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from system_prompt import SYSTEM_PROMPT

# ============================================
# CONFIGURATION
# ============================================
load_dotenv()

# Initialize Groq client
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception as e:
    st.error(f"Error initializing Groq: {e}")
    st.stop()

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="StartupLaunch AI - Startup Idea Validator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# LOAD CUSTOM CSS
# ============================================
def load_css():
    css_file = "assets/style.css"
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("Custom CSS file not found. Using default styles.")

load_css()

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    # Logo section
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 2.5rem; margin: 0;'>🚀</h1>
        <h2 style='margin: 10px 0; font-size: 1.5rem; color: #667eea;'>StartupLaunch AI</h2>
        <p style='color: #9ca3af; font-size: 0.85rem;'>Your AI Business Advisor</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # What I can do section
    st.markdown("### 🎯 Core Features")
    
    features = [
        ("💡", "Idea Validation", "Check feasibility & market fit"),
        ("📊", "Market Analysis", "Target audience & market size"),
        ("🏆", "Competitor Intel", "Identify & analyze competition"),
        ("📋", "SWOT Analysis", "Strategic business analysis"),
        ("🛠️", "MVP Planning", "Define core features"),
        ("💰", "Revenue Models", "Monetization strategies"),
        ("🧑‍💻", "Tech Stack", "Technology recommendations"),
        ("💵", "Budget Estimate", "Cost projections"),
        ("📑", "Pitch Deck", "Investor presentation outline"),
        ("🏷️", "Naming Ideas", "Creative brand names"),
        ("⚠️", "Risk Assessment", "Identify potential risks"),
        ("📢", "Go-to-Market", "Launch strategy")
    ]
    
    for icon, title, desc in features:
        st.markdown(f"""
        <div style='margin: 10px 0; padding: 10px; background: rgba(255,255,255,0.03); 
                    border-radius: 8px; border-left: 3px solid #667eea;'>
            <div style='font-size: 1.1rem; margin-bottom: 3px;'>
                <span style='margin-right: 8px;'>{icon}</span>
                <strong style='color: #e5e7eb;'>{title}</strong>
            </div>
            <div style='font-size: 0.8rem; color: #9ca3af; margin-left: 28px;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # AI Model info
    st.markdown("### ⚙️ AI Engine")
    st.markdown("""
    <div style='background: rgba(102, 126, 234, 0.1); padding: 15px; border-radius: 10px;
                border: 1px solid rgba(102, 126, 234, 0.3);'>
        <div style='font-size: 1.1rem; font-weight: 600; color: #667eea; margin-bottom: 5px;'>
            🤖 LLaMA 3.3 70B
        </div>
        <div style='font-size: 0.85rem; color: #b8b8d1;'>
            Powered by <strong>Groq</strong><br>
            Ultra-fast inference<br>
            Advanced reasoning
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 New Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("💡 Examples", use_container_width=True):
            st.session_state.show_examples = not st.session_state.get('show_examples', False)
            st.rerun()
    
    st.markdown("---")
    
    # Session stats
    if len(st.session_state.get('messages', [])) > 1:
        st.markdown("### 📈 Session Stats")
        user_msgs = len([m for m in st.session_state.messages if m['role'] == 'user'])
        
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px;'>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; font-weight: 700; color: #667eea;'>{user_msgs}</div>
                <div style='font-size: 0.9rem; color: #9ca3af;'>Messages Sent</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; padding: 20px 0; color: #6b7280; font-size: 0.8rem;'>
        <div style='margin-bottom: 5px;'>Built with ❤️ using</div>
        <div style='font-weight: 600; color: #667eea;'>Groq AI • Streamlit</div>
        <div style='margin-top: 10px; font-size: 0.75rem;'>🔒 Your data is private & secure</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# INITIALIZE SESSION STATE
# ============================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_examples" not in st.session_state:
    st.session_state.show_examples = False

# ============================================
# MAIN HEADER
# ============================================
st.markdown("""
<div class='main-header-container'>
    <h1 class='startup-title'>🚀 StartupLaunch AI</h1>
    <p class='startup-subtitle'>Validate • Analyze • Launch Your Startup Idea with AI-Powered Insights</p>
    <div class='feature-badges'>
        <span class='badge'>💡 Idea Validation</span>
        <span class='badge'>📊 Market Analysis</span>
        <span class='badge'>🏆 Competitor Research</span>
        <span class='badge'>🛠️ MVP Planning</span>
        <span class='badge'>💰 Revenue Strategy</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# EXAMPLE PROMPTS SECTION
# ============================================
if st.session_state.show_examples:
    st.markdown("### 💡 Example Startup Ideas - Click to Use")
    
    example_prompts = [
        {
            "title": "🏠 Student Housing Platform",
            "prompt": "I want to build an app that helps college students find affordable PG accommodations near their campus with verified reviews and virtual tours"
        },
        {
            "title": "🌾 Farm-to-Consumer Marketplace",
            "prompt": "Validate my idea: A platform connecting local farmers directly with urban consumers for fresh organic produce delivery"
        },
        {
            "title": "🍲 Home-Cooked Meal Delivery",
            "prompt": "I'm planning a food delivery service that connects home cooks with office workers for healthy, home-style meals"
        },
        {
            "title": "💪 AI Fitness Coach",
            "prompt": "Build a fitness app that uses AI to create personalized workout plans for busy professionals who can't afford personal trainers"
        },
        {
            "title": "📚 Peer Learning Platform",
            "prompt": "Create a platform where students can teach and learn from each other, earning money while helping peers"
        },
        {
            "title": "♻️ Sustainable Fashion Marketplace",
            "prompt": "Launch an online marketplace for buying, selling, and renting pre-owned designer clothing and accessories"
        }
    ]
    
    cols = st.columns(2)
    for idx, example in enumerate(example_prompts):
        with cols[idx % 2]:
            if st.button(f"{example['title']}", key=f"ex_{idx}", use_container_width=True):
                st.session_state.example_selected = example['prompt']
                st.session_state.show_examples = False
                st.rerun()

# ============================================
# WELCOME MESSAGE
# ============================================
if not st.session_state.messages:
    welcome_msg = """
### 👋 Welcome to StartupLaunch AI!

I'm your **AI-powered startup advisor** built on **LLaMA 3.3 70B** via Groq! 

#### 🎯 How I Help You Succeed:

| **Service** | **What You Get** |
|------------|-----------------|
| 💡 **Idea Validation** | Assess feasibility, market demand, and success potential |
| 📊 **Market Analysis** | Target audience profiling, market size (TAM/SAM/SOM), trends |
| 🏆 **Competitor Intelligence** | Identify direct/indirect competitors, differentiation strategies |
| 📋 **SWOT Analysis** | Comprehensive strategic analysis of your business |
| 🛠️ **MVP Planning** | Define must-have features for your first version |
| 💰 **Revenue Strategy** | Explore monetization models (SaaS, marketplace, freemium, etc.) |
| 🧑‍💻 **Tech Stack** | Get technology recommendations for your product |
| 💵 **Budget Estimation** | Realistic cost projections for development & marketing |
| 📑 **Pitch Deck Outline** | Structure to impress investors and raise funding |
| 🏷️ **Brand Naming** | Creative, memorable, and brandable name suggestions |

---

#### 🚀 Ready to Get Started?

**Simply describe your startup idea below**, or click **💡 Examples** in the sidebar for inspiration!

> **Example:** *"I want to create a mobile app that uses AI to help people reduce food waste by suggesting recipes based on leftover ingredients"*

**What's your big idea? Let's validate it together! 💭**
"""
    st.session_state.messages.append({
        "role": "assistant", 
        "content": welcome_msg
    })

# ============================================
# DISPLAY CHAT MESSAGES
# ============================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================
# HANDLE EXAMPLE SELECTION
# ============================================
if "example_selected" in st.session_state:
    user_input = st.session_state.example_selected
    del st.session_state.example_selected
    
    # Add user message
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input
    })
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🚀 Analyzing your startup idea..."):
            try:
                groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                
                for msg in st.session_state.messages:
                    if msg["role"] in ["user", "assistant"]:
                        groq_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=groq_messages,
                    temperature=0.7,
                    max_tokens=2048,
                    top_p=0.9
                )
                
                assistant_response = response.choices[0].message.content
                st.markdown(assistant_response)
                
            except Exception as e:
                assistant_response = f"⚠️ **Error:** {str(e)}\n\nPlease check your API configuration and try again."
                st.error(assistant_response)
    
    st.session_state.messages.append({
        "role": "assistant", 
        "content": assistant_response
    })
    
    st.rerun()

# ============================================
# CHAT INPUT
# ============================================
if user_input := st.chat_input("💡 Describe your startup idea or ask me anything..."):
    
    # Display user message
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input
    })
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("🚀 Analyzing your idea..."):
            try:
                # Prepare Groq messages
                groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                
                # Add last 10 messages for context
                recent_messages = st.session_state.messages[-10:]
                for msg in recent_messages:
                    if msg["role"] in ["user", "assistant"]:
                        groq_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
                
                # Call Groq API
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=groq_messages,
                    temperature=0.7,
                    max_tokens=2048,
                    top_p=0.9,
                    stream=False
                )
                
                assistant_response = response.choices[0].message.content
                st.markdown(assistant_response)
                
            except Exception as e:
                error_msg = str(e)
                
                if "rate_limit" in error_msg.lower():
                    assistant_response = """
⚠️ **Rate Limit Reached**

You're sending messages too quickly. Please wait 10-20 seconds and try again.

**Groq Free Tier Limits:**
- 30 requests per minute
- 14,400 requests per day

Take a quick break and we'll continue! ☕
"""
                elif "authentication" in error_msg.lower():
                    assistant_response = """
⚠️ **Authentication Error**

There's an issue with the API configuration. Please verify:
1. GROQ_API_KEY is set correctly in `.env`
2. The API key is valid
3. No extra spaces or quotes

Contact support if the issue persists.
"""
                else:
                    assistant_response = f"""
⚠️ **Unexpected Error**

**Quick fixes:**
1. Check internet connection
2. Refresh the page
3. Try again in a moment

Still stuck? Let me know and I'll help troubleshoot!
"""
                
                st.error(assistant_response)
    
    # Save response
    st.session_state.messages.append({
        "role": "assistant", 
        "content": assistant_response
    })