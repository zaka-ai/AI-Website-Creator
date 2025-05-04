import streamlit as st
import base64
from generator import WebsiteGenerator
from utils.parser import parse_code_blocks
from utils.aggregator import combine_code
from streamlit.components.v1 import html as components_html

# Set page config with custom sidebar width
st.set_page_config(
    page_title="WebGenie - AI Website Builder",
    page_icon="🧞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling with fixed sidebar width
st.markdown("""
<style>
    /* Fixed sidebar width (1/3 of page) */
    section[data-testid="stSidebar"] {
        width: 33% !important;
        min-width: 33% !important;
        max-width: 33% !important;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #f8f9fa !important;
    }
    .stSelectbox>div>div>select {
        background-color: #f8f9fa !important;
    }
    .stSlider>div>div>div>div {
        background-color: #f8f9fa !important;
    }
    .css-1aumxhk {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
    }
    .download-btn {
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 8px 16px !important;
        border-radius: 4px !important;
        text-decoration: none !important;
        margin-right: 10px !important;
    }
    .download-btn:hover {
        background-color: #45a049 !important;
    }
    .color-picker-row {
        display: flex;
        gap: 20px;
        margin-bottom: 1rem;
    }
    .divider {
        margin: 1.5rem 0;
        border-top: 1px solid #e6e6e6;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        color: #4F46E5;
    }
    .coming-soon {
        color: #999;
        font-style: italic;
        font-size: 0.9rem;
    }
    .model-select-container {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def create_download_button(content, filename, label):
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/{filename.split(".")[-1]};base64,{b64}" download="{filename}" class="download-btn">{label}</a>'
    return href

def main():
    st.title("🧞 WebGenie - AI Website Builder")
    st.markdown("Create beautiful websites in seconds with the power of AI!")
    
    # Model options with availability indicators
    MODEL_OPTIONS = {
        "Qwen2.5-Coder-14B (Fine-tuned)": "supported",
        "OpenAI GPT-4 Turbo": "coming-soon",
        "Llama 3 8B": "coming-soon",
        "Mistral 7B": "coming-soon",
        "Gemma 7B": "coming-soon"
    }
    
    with st.expander("⚙️ Website Configuration", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-title" style="margin-bottom: 0.75rem;">Model Selection</div>', unsafe_allow_html=True)
            selected_model = st.selectbox(
                "Select AI Model",
                options=list(MODEL_OPTIONS.keys()),
                format_func=lambda x: f"{x} {'(Coming Soon)' if MODEL_OPTIONS[x] == 'coming-soon' else ''}"
            )
            
            if MODEL_OPTIONS[selected_model] == "coming-soon":
                st.markdown('<div class="coming-soon" style="margin-top: -0.5rem; margin-bottom: 1rem;">This model will be available in a future update</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="margin-bottom: 1rem;"></div>', unsafe_allow_html=True)  # Spacer for consistent layout
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">Website Content</div>', unsafe_allow_html=True)
            website_description = st.text_area(
                "Describe your website",
                placeholder="I want a modern landing page for a SaaS product that helps with project management...",
                height=150
            )
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">Color Scheme</div>', unsafe_allow_html=True)
            st.markdown('<div class="color-picker-row">', unsafe_allow_html=True)
            primary_color = st.color_picker("Primary Color", "#4F46E5")
            secondary_color = st.color_picker("Secondary Color", "#10B981")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="section-title">Typography</div>', unsafe_allow_html=True)
            font_family = st.selectbox(
                "Font Family",
                ["Inter", "Roboto", "Open Sans", "Montserrat", "Poppins", "Nunito"]
            )
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">Layout & Style</div>', unsafe_allow_html=True)
            layout_style = st.selectbox(
                "Layout Style",
                ["Modern", "Minimalist", "Corporate", "Creative", "Elegant", "Bold"]
            )
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">Features</div>', unsafe_allow_html=True)
            include_animation = st.checkbox("Include Animations", value=False)
            dark_mode = st.checkbox("Dark Mode Support", value=False)
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">Structure</div>', unsafe_allow_html=True)
            num_sections = st.slider("Number of Sections", 1, 6, 3)
    
    generate_button = st.button("✨ Generate Website", use_container_width=True,
                              disabled=MODEL_OPTIONS[selected_model] == "coming-soon")
    
    # Sidebar for preview
    st.sidebar.title("Generated Website Preview")
    st.sidebar.markdown("Your website will appear here after generation.")
    
    if generate_button and website_description:
        with st.spinner("🧞 WebGenie is crafting your website..."):
            # Prepare the prompt configuration
            prompt_config = {
                "description": website_description,
                "primary_color": primary_color,
                "secondary_color": secondary_color,
                "font_family": font_family,
                "layout_style": layout_style,
                "include_animation": include_animation,
                "dark_mode": dark_mode,
                "num_sections": num_sections,
                "model": selected_model
            }
            
            try:
                # Initialize generator and create website
                generator = WebsiteGenerator()
                code_blocks = generator.generate_website(prompt_config)
                
                if code_blocks:
                    # Combine code for preview
                    combined_html = combine_code(
                        code_blocks.get("html", ""),
                        code_blocks.get("css", ""),
                        code_blocks.get("javascript", "")
                    )
                    
                    # Display the website preview in sidebar
                    st.sidebar.empty()  # Clear previous content
                    st.sidebar.title("Website Preview")
                    
                    # Use components.html with iframe for better isolation
                    with st.sidebar:
                        components_html(
                            f"""
                            <iframe srcdoc='{combined_html.replace("'", "&apos;")}' 
                                    style='width:100%; height:800px; border:none;'>
                            </iframe>
                            """,
                            height=820
                        )
                    
                    # Display success message
                    st.success("🎉 Website generated successfully!")
                    
                    # Add divider
                    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                    
                    # Download section
                    st.subheader("Download Your Website Code")
                    
                    # Create tabs for code viewing
                    tab1, tab2, tab3 = st.tabs(["HTML", "CSS", "JavaScript"])
                    
                    with tab1:
                        st.code(code_blocks.get("html", ""), language="html")
                        st.markdown(
                            create_download_button(
                                code_blocks.get("html", ""), 
                                "index.html", 
                                "⬇️ Download HTML"
                            ),
                            unsafe_allow_html=True
                        )
                    
                    with tab2:
                        st.code(code_blocks.get("css", ""), language="css")
                        st.markdown(
                            create_download_button(
                                code_blocks.get("css", ""),
                                "styles.css",
                                "⬇️ Download CSS"
                            ),
                            unsafe_allow_html=True
                        )
                    
                    with tab3:
                        st.code(code_blocks.get("javascript", ""), language="javascript")
                        st.markdown(
                            create_download_button(
                                code_blocks.get("javascript", ""),
                                "script.js",
                                "⬇️ Download JS"
                            ),
                            unsafe_allow_html=True
                        )
                    
                    # Add success footer
                    st.markdown("---")
                    st.markdown(
                        """<div style="text-align: center; color: #4F46E5; font-weight: bold;">
                        Your website is ready! 🎉
                        </div>""",
                        unsafe_allow_html=True
                    )
                    
                else:
                    st.error("❌ Failed to generate website code. Please try again.")
                    
            except Exception as e:
                st.error(f"""
                ❌ An error occurred during generation:
                ```
                {str(e)}
                ```
                Please check your inputs and try again.
                """)
                
    elif generate_button:
        st.warning("⚠️ Please provide a website description to generate your website.")

if __name__ == "__main__":
    main()