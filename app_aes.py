import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import base64

# --- 1. FUNGSI LOGIKA BACKEND (AES-256 GCM) ---

def get_aes_key(user_key_string):
    """Menghasilkan kunci AES 256-bit (32 bytes) dari string input menggunakan hashing SHA256."""
    hash_object = SHA256.new(user_key_string.encode('utf-8'))
    return hash_object.digest()

def aes_encrypt(plaintext, user_key):
    """Fungsi enkripsi AES-256 GCM."""
    try:
        key = get_aes_key(user_key)
        nonce = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
        encrypted_data = base64.b64encode(nonce + ciphertext + tag).decode('utf-8')
        return encrypted_data
        
    except Exception as e:
        return f"ENKRIPSI GAGAL: {e}"

def aes_decrypt(encrypted_data, user_key):
    """Fungsi dekripsi AES-256 GCM."""
    try:
        key = get_aes_key(user_key)
        raw_data = base64.b64decode(encrypted_data.encode('utf-8'))
        
        nonce = raw_data[:16]
        ciphertext = raw_data[16:-16]
        tag = raw_data[-16:]
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        
        return plaintext.decode('utf-8')
        
    except ValueError as e:
        return "DEKRIPSI GAGAL: Kunci salah atau Data telah dirusak."
    except Exception as e:
        return f"DEKRIPSI GAGAL: {e}"


# --- 2. TAMPILAN FRONTEND (STREAMLIT UI) ---

st.set_page_config(
    page_title="AES Project UTS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Kustom untuk Tampilan Pink Soft dan Keterbacaan Tinggi
st.markdown(
    """
    <style>
    /* Latar belakang Pink Soft (MistyRose) */
    .stApp {
        background-color: #ffe4e1; 
        color: #1a1a1a; /* Warna teks dasar diubah menjadi hitam gelap */
    }
    
    /* Warna teks dasar */
    p, label, .stMarkdown {
        color: #1a1a1a !important; 
    }

    /* Styling Tombol Umum */
    .stButton>button {
        border-radius: 15px; 
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }

    /* Modifikasi Khusus Tombol DEKRIPSI (Putih dengan Teks Hitam) */
    div[data-testid="stColumn"]:nth-child(2) .stButton>button {
        background-color: white; 
        color: black;
        border: 2px solid #ff69b4; /* Tambah garis pink agar lebih menonjol */
    }

    /* Styling Judul */
    h1 {
        color: #800080; /* Purple gelap untuk kontras tinggi */
        text-shadow: 1px 1px #ccc;
    }
    
    /* MODIFIKASI: Input area (textarea dan password) diubah menjadi putih murni */
    textarea, input[type="password"] {
        color: black !important;
        background-color: white !important; /* Putih Murni */
        border: 1px solid #ff69b4; /* Tambah garis tepi pink agar menonjol dari latar */
    }

    h3 {
        color: #4b0082; 
    }

    </style>
    """, 
    unsafe_allow_html=True
)
# Akhir CSS Kustom

st.title("🔐 Proyek Enkripsi Rahasia (AES-256) 🦊")
st.subheader("🛡️ Kriptografi Level Industri untuk UTS!")
st.warning("⚠️ Algoritma AES-256 (Mode GCM) digunakan. Pastikan Kata Kunci tidak hilang!")

# Input Kunci (Disembunyikan)
key_input = st.text_input(
    "Masukkan Kata Kunci/Password (Kunci AES 256):", 
    type="password"
)

# Input Teks
text_input = st.text_area("Masukkan Teks Input:", height=150)

# Kolom untuk Tombol
col1, col2 = st.columns(2)

# --- 3. HANDLE AKSI TOMBOL & OUTPUT ---

if col1.button("ENKRIPSI (AES)", use_container_width=True, type="primary"):
    if text_input and key_input:
        result = aes_encrypt(text_input, key_input)
        
        if result.startswith("ENKRIPSI GAGAL"):
             st.error(result)
        else:
            st.balloons()
            st.success("🎉 **ENKRIPSI AES BERHASIL!** Pesanmu Aman! 🥳")
            st.code(result, language='text')
            st.caption("Output (Base64) terdiri dari Nonce, Ciphertext, dan Tag Otentikasi.")
    else:
        st.error("⚠️ Harap isi Teks Input dan Kata Kunci.")

if col2.button("DEKRIPSI (AES)", use_container_width=True, type="secondary"):
    if text_input and key_input:
        result = aes_decrypt(text_input, key_input)
        
        if result.startswith("DEKRIPSI GAGAL"):
             st.error(result)
        else:
            st.success("✅ **DEKRIPSI AES SELESAI!**")
            st.code(result, language='text')
            st.caption("Hasil Dekripsi Kembali ke Teks Asli.")
    else:
        st.error("⚠️ Harap isi Teks Input dan Kata Kunci.")

st.markdown("---")
st.subheader("🔑 Rangkuman Teknis (Untuk Presentasi)")
st.markdown("""
* **Backend Logic:** Semua fungsi enkripsi, hashing, dan verifikasi berjalan di server Python (memenuhi syarat 'fungsi backend').
* **Standar Industri:** Menggunakan **AES-256** dan **Mode GCM** (termasuk Tag Otentikasi).
* **Poin Plus:** Program mampu mendeteksi jika *ciphertext* dirusak atau kunci salah, menunjukkan integritas data yang tinggi.
""")