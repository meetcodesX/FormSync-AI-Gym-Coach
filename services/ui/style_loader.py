import os
import streamlit as st
import streamlit.components.v1 as components
import base64
 

def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def inject_webrtc_styles():
    components.html("""
    <script>
    (function patchWebRTCStyles() {
        function injectIntoIframe(iframe) {
            try {
                const doc = iframe.contentDocument || iframe.contentWindow.document;
                if (!doc || !doc.head) return;
                if (doc.head.querySelector('#webrtc-custom-styles')) return;

                const style = doc.createElement('style');
                style.id = 'webrtc-custom-styles';
                style.textContent = `
                    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700&display=swap');

                    .MuiButtonBase-root,
                    .MuiButton-root,
                    .MuiButton-contained,
                    .MuiButton-text {
                        border-radius: 0 !important;
                        font-family: 'Rubik', sans-serif !important;
                        letter-spacing: 0.05em !important;
                    }
                `;
                doc.head.appendChild(style);
            } catch (e) {
                console.warn('[patcher] could not inject:', e);
            }
        }

        function findAndPatch() {
            const parentDoc = window.parent.document;
            const iframes = parentDoc.querySelectorAll('iframe');

            iframes.forEach(iframe => {
                if (iframe.src && iframe.src.includes('webrtc')) {
                    if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {
                        injectIntoIframe(iframe);
                    } else {
                        iframe.addEventListener('load', () => injectIntoIframe(iframe));
                    }
                }
            });
        }

        findAndPatch();
    })();
    </script>
    """, height=0)