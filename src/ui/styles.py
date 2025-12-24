"""
UI样式模块 - Styles
定义Gradio界面的CSS样式
"""

# 完整的CSS样式定义
CUSTOM_CSS = """
/* Import modern fonts including Microsoft YaHei for elegant typography */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* Fallback for Microsoft YaHei */
@font-face {
  font-family: 'Microsoft YaHei';
  src: local('Microsoft YaHei'), url('https://fonts.cdnfonts.com/css/microsoft-yahei') format('woff');
}

/* Root variables for colors, radii, shadows - enhanced for 2025 trends */
:root {
  --bg-gradient: linear-gradient(180deg, #fdf5eb 0%, #fef0e0 40%, #fff7ef 100%);
  --primary-color: #1f2937;
  --secondary-color: #6b7280;
  --shadow-drop: 0 10px 30px rgba(208, 180, 140, 0.15);
  --shadow-inset: inset 0 2px 4px rgba(0, 0, 0, 0.05);
  --radius-lg: 32px;
  --radius-md: 24px;
  --radius-sm: 16px;
  --accent-purple: #7c3aed;
  --accent-gradient: linear-gradient(135deg, #7c3aed, #a855f7);
  --text-dark: #3c2f21;
  --text-muted: #6b7280;
  --transition-fast: all 0.2s ease-in-out;
  --transition-smooth: all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

/* Base container styling */
.gradio-container {
  background: var(--bg-gradient);
  color: var(--primary-color);
  font-family: 'Microsoft YaHei', 'Inter', 'Noto Serif SC', sans-serif;
  max-width: 1440px;
  margin: 0 auto;
  padding: 2rem;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-drop);
}

/* Hero section */
.hero {
  margin-bottom: 2rem;
  padding: 3.5rem 3rem;
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.92), rgba(255, 245, 230, 0.95));
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-drop), var(--shadow-inset);
  color: var(--text-dark);
  text-align: center;
  transition: var(--transition-smooth);
}

.hero:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 40px rgba(208, 180, 140, 0.25);
}

.hero h1 {
  font-size: clamp(2rem, 5vw, 3rem);
  margin-bottom: 1rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: black;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero p {
  margin: 0.5rem 0;
  font-size: clamp(1rem, 3vw, 1.15rem);
  color: var(--text-muted);
}

.hero .badge-line {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin-top: 1.5rem;
}

.hero .badge {
  padding: 0.5rem 1.2rem;
  border-radius: 999px;
  font-size: 0.95rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(8px);
  color: var(--accent-purple);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.15);
  transition: var(--transition-fast);
}

.hero .badge:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(124, 58, 237, 0.25);
}

/* Page layout */
.page-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: start;
}

@media (max-width: 1200px) {
  .page-layout {
    grid-template-columns: 1fr;
  }
}

/* Panel cards */
.panel-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.98), rgba(255, 250, 245, 0.98));
  border-radius: var(--radius-lg);
  padding: 2rem 2.2rem;
  box-shadow: var(--shadow-drop), var(--shadow-inset);
  margin-bottom: 2rem;
  transition: var(--transition-smooth);
}

.panel-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 40px rgba(208, 180, 140, 0.25);
}

/* Analysis section */
.analysis-heading {
  font-size: 1.3rem;
  font-weight: 600;
  color: black;
  margin-bottom: 1rem;
  text-align: center;
}

.analysis-stack {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.analysis-pill {
  padding: 0.8rem 1.2rem;
  border-radius: var(--radius-md);
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  box-shadow: var(--shadow-drop);
  font-size: 1rem;
  line-height: 1.3;
  transition: var(--transition-fast);
}

.analysis-pill:hover {
  transform: translateY(-2px);
}

.analysis-pill strong {
  font-weight: 600;
}

.tone-pill { background: linear-gradient(135deg, #fdeee2, #f8d9c5); color: #cc6f2b; }
.scene-pill { background: linear-gradient(135deg, #e6f6ed, #d1f0df); color: #1f7a55; }
.mood-pill { background: linear-gradient(135deg, #e8f1ff, #d4e5ff); color: #1d4ed8; }
.recommend-pill { background: linear-gradient(135deg, #f2e8ff, #e3d1ff); color: var(--accent-purple); font-weight: 600; }

/* Image frame */
.image-frame .gr-image {
  border-radius: var(--radius-lg);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.9), 0 12px 35px rgba(60, 64, 67, 0.12);
  overflow: hidden;
}

.image-frame .gr-image img {
  object-fit: cover;
  border-radius: var(--radius-lg);
  transition: var(--transition-smooth);
}

.image-frame .gr-image:hover img {
  transform: scale(1.02);
}

/* Section titles */
.section-title {
  font-size: 1.35rem;
  font-weight: 600;
  color: black;
  margin-bottom: 1rem;
  text-align: center;
  letter-spacing: 0.02em;
}

.section-subtitle {
  color: var(--text-muted);
  font-size: 1rem;
  margin-bottom: 1.2rem;
  display: block;
  text-align: center;
  font-style: italic;
}

/* Card radio */
.card-radio .gr-radio {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.card-radio .gr-radio label {
  flex: 1 1 180px;
  background: linear-gradient(145deg, #ffffff, #f9f9f9);
  border-radius: var(--radius-md);
  border: 1px solid rgba(0, 0, 0, 0.05);
  padding: 1.2rem 1.4rem;
  box-shadow: var(--shadow-drop);
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  transition: var(--transition-fast);
  cursor: pointer;
}

.card-radio .gr-radio label:hover {
  border-color: var(--accent-purple);
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(124, 58, 237, 0.15);
}

.card-radio .gr-radio input {
  display: none;
}

.card-radio .gr-radio label span {
  font-size: 1.05rem;
  color: var(--primary-color);
}

.card-radio .gr-radio label:has(input:checked) {
  border-color: var(--accent-purple);
  background: linear-gradient(145deg, #f9f5ff, #f0eaff);
  box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.1), var(--shadow-drop);
}

.card-radio .gr-radio label:has(input:checked) span {
  color: var(--accent-purple);
  font-weight: 600;
}

.card-hint {
  margin-top: 0.6rem;
  color: var(--text-muted);
  font-size: 0.95rem;
  text-align: center;
  opacity: 0.9;
}

/* Output card */
.output-card .gr-chatbot {
  border-radius: var(--radius-md);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.92), rgba(248, 250, 252, 0.92));
  box-shadow: var(--shadow-inset);
  padding: 1rem;
}

.output-card .gr-chatbot .wrap {
  background-color: transparent !important;
}

.output-card .gr-chatbot .wrap > * {
  background-color: rgba(255, 255, 255, 0.95) !important;
  border-radius: var(--radius-sm);
  padding: 1rem;
  margin-bottom: 1rem;
}

.poem-output textarea {
  background: linear-gradient(145deg, #fff7e7, #fff0d9);
  border-radius: var(--radius-md) !important;
  border: 1px solid rgba(251, 211, 141, 0.4) !important;
  box-shadow: var(--shadow-inset);
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--text-dark);
  resize: none;
}

.poem-output label {
  font-weight: 500;
  color: var(--text-muted);
}

/* Suggestion box */
.suggestion-box {
  background: linear-gradient(145deg, #f3f4f6, #e5e7eb);
  border-radius: var(--radius-lg);
  padding: 1.3rem;
  margin-top: 1.2rem;
  box-shadow: var(--shadow-drop);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.suggestion-box .gr-button {
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  padding: 0.6rem 1.2rem;
  background: var(--accent-gradient);
  border: none;
  color: white;
  transition: var(--transition-fast);
}

.suggestion-box .gr-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(124, 58, 237, 0.2);
}

/* Recent grid */
.recent-grid {
  display: grid;
  gap: 1.3rem;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

.recent-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.98), rgba(248, 250, 252, 0.98));
  border-radius: var(--radius-lg);
  padding: 1.3rem;
  box-shadow: var(--shadow-drop);
  border: 1px solid rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  transition: var(--transition-smooth);
}

.recent-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 40px rgba(188, 170, 145, 0.2);
}

.recent-card img {
  width: 100%;
  border-radius: var(--radius-md);
  object-fit: cover;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
}

.recent-card .recent-title {
  font-weight: 600;
  color: var(--accent-purple);
}

.recent-card .recent-meta {
  font-size: 0.9rem;
  color: var(--text-muted);
}

.recent-card .recent-history {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-dark);
}

.recent-empty {
  text-align: center;
  color: var(--text-muted);
  font-size: 1rem;
  background: linear-gradient(145deg, #f3f4f6, #e5e7eb);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-inset);
}

/* Footer */
.footer {
  margin-top: 2.5rem;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.95rem;
  opacity: 0.8;
}

/* Global enhancements */
* {
  box-sizing: border-box;
  scroll-behavior: smooth;
}
"""