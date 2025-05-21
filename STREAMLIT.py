import streamlit as st
import pandas as pd
import pickle

# Halaman Pendahuluan
def show_pendahuluan():
    st.title("Pendahuluan")

    st.markdown("""
    ### Latar Belakang
    Manajemen Pemasaran sebuah perusahaan telekomunikasi menghadapi tantangan besar terkait tingkat churn pelanggan yang cukup tinggi. Mereka selama ini mengeluarkan biaya promosi ke seluruh pelanggan tanpa tahu siapa yang benar-benar berisiko berhenti menggunakan layanan. Strategi ini tidak efisien, karena sebagian besar promosi justru jatuh kepada pelanggan loyal yang sebenarnya tidak berniat berhenti.

    Sebagai Data Scientist perusahaan, diberi tugas oleh Manajemen Pemasaran untuk mengembangkan model machine learning yang mampu memprediksi apakah seorang pelanggan akan melakukan churn atau tidak. Dengan model ini, diharapkan perusahaan:
    - Dapat mengidentifikasi pelanggan yang berpotensi churn sebelum mereka benar-benar pergi.
    - Dapat mengoptimalkan biaya promosi, hanya diberikan kepada pelanggan yang benar-benar membutuhkan.
    - Dapat mengurangi kerugian dari kehilangan pelanggan setia.

    ### Rumusan Masalah / Problem Statement
    Perusahaan telekomunikasi menghadapi tantangan dalam mempertahankan pelanggan setia di tengah persaingan industri yang semakin ketat. Customer churn atau berhentinya pelanggan menggunakan layanan, dapat menyebabkan kerugian finansial yang signifikan, terutama jika pelanggan yang churn tidak terdeteksi lebih awal.

    Saat ini, perusahaan tidak memiliki sistem yang mampu memprediksi kemungkinan pelanggan akan berhenti berlangganan. Akibatnya, strategi promosi dilakukan secara massal ke seluruh pelanggan, yang mengakibatkan biaya promosi yang besar namun tidak efisien.

    Diperlukan sebuah sistem berbasis Machine Learning untuk membantu perusahaan dalam:
    - Memprediksi lebih dini siapa saja pelanggan yang kemungkinan akan churn,
    - Meminimalkan kehilangan pelanggan dengan memberikan promosi tepat sasaran hanya kepada mereka yang berisiko churn,
    - Mengurangi pemborosan biaya promosi kepada pelanggan yang sebenarnya tidak akan churn.

    ### Metric Evaluation
    - Cost FP: $100  
    - Cost FN: $500

    False Positive (FP): Model memprediksi seorang customer akan churn → perusahaan memberi promosi senilai $100, tetapi sebenarnya customer tidak churn.  
    → Biaya promosi sia-sia.

    False Negative (FN): Model memprediksi customer tidak akan churn → perusahaan tidak melakukan tindakan, tetapi sebenarnya customer churn.  
    → Perusahaan kehilangan customer dengan potensi kerugian $500.

    Karena cost dari FN jauh lebih tinggi dibanding FP, maka F2-score dipilih sebagai metrik evaluasi utama, karena F2-score memberikan lebih banyak bobot ke recall.

    ### Tujuan / Goals
    1. **Memprediksi Churn Pelanggan**  
       Mengembangkan model Machine Learning yang dapat mengidentifikasi pelanggan yang berpotensi churn berdasarkan data historis pelanggan.

    2. **Mengurangi Kerugian Finansial**  
       Membantu perusahaan mengurangi biaya akibat kehilangan pelanggan (False Negative) yang memiliki dampak finansial besar ($500 per pelanggan) dengan memberikan penanganan preventif.

    3. **Mengoptimalkan Strategi Promosi**  
       Mengurangi pemborosan promosi kepada pelanggan loyal (False Positive) yang sebenarnya tidak akan churn ($100 per pelanggan) dengan hanya menargetkan pelanggan yang benar-benar berisiko churn.

    4. **Menggunakan Metode Evaluasi yang Tepat**  
       Menggunakan metrik F2 Score sebagai acuan utama untuk mengevaluasi model, karena memberikan penekanan lebih besar pada minimisasi False Negative.

    5. **Memberikan Insight Fitur Penting**  
       Mengidentifikasi fitur-fitur yang paling berkontribusi terhadap keputusan churn agar perusahaan dapat melakukan intervensi bisnis yang lebih tepat sasaran.
    """)

# Fungsi halaman penjelasan fitur
def show_feature_info():
    st.title("Penjelasan Fitur Telco Customer Churn")

    st.markdown("""
    #### 1. Dependents
    - Definisi: Menunjukkan apakah pelanggan memiliki tanggungan (anak, pasangan, atau anggota keluarga lain).
    - Tipe data: `object` (kategorikal)
    - Nilai unik: `Yes`, `No`
      - `Yes` → Pelanggan memiliki tanggungan.
      - `No` → Tidak memiliki tanggungan.
    ---
    #### 2. tenure
    - Definisi: Lama waktu (dalam bulan) pelanggan telah berlangganan.
    - Tipe data: `int64` (numerik)
    - Contoh nilai: `16`, `9`, `18` (73 nilai unik)
      - Angka lebih tinggi berarti pelanggan lebih lama berlangganan.
    ---
    #### 3. OnlineSecurity
    - Definisi: Apakah pelanggan memiliki layanan keamanan online.
    - Tipe data: `object`
    - Nilai unik: `Yes`, `No`, `No internet service`
    ---
    #### 4. OnlineBackup
    - Definisi: Apakah pelanggan memiliki layanan backup data online.
    - Tipe data: `object`
    - Nilai unik: `Yes`, `No`, `No internet service`
    ---
    #### 5. InternetService
    - Definisi: Jenis layanan internet yang dimiliki pelanggan.
    - Tipe data: `object`
    - Nilai unik: `DSL`, `Fiber optic`, `No`
    ---
    #### 6. DeviceProtection
    - Definisi: Apakah pelanggan memiliki perlindungan perangkat.
    - Tipe data: `object`
    - Nilai unik: `Yes`, `No`, `No internet service`
    ---
    #### 7. TechSupport
    - Definisi: Apakah pelanggan memiliki dukungan teknis dari penyedia.
    - Tipe data: `object`
    - Nilai unik: `Yes`, `No`, `No internet service`
    ---
    #### 8. Contract
    - Definisi: Jenis kontrak berdasarkan durasi langganan.
    - Tipe data: `object`
    - Nilai unik: `Month-to-month`, `One year`, `Two year`
    ---
    #### 9. PaperlessBilling
    - Definisi: Apakah pelanggan menggunakan tagihan tanpa kertas.
    - Tipe data: `object`
    - Nilai unik: `Yes`, `No`
    ---
    #### 10. MonthlyCharges
    - Definisi: Jumlah biaya langganan bulanan.
    - Tipe data: `float64`
    - Nilai unik: 1422 (nilai numerik kontinu)
    ---
    #### 11. Churn
    - Definisi: Target variabel — apakah pelanggan berhenti berlangganan atau tidak.
    - Tipe data: `object`
    - Nilai unik: `Yes` -> 1, `No` -> 0
    """)

# Fungsi halaman prediksi churn
def show_prediction():
    st.title("Telco Customer Churn Prediction")

    st.sidebar.header("Input Customer Features")

    def input_user():
        Dependents = st.sidebar.radio("Dependents", ["Yes", "No"])
        tenure = st.sidebar.number_input("Tenure (in months)", min_value=1, max_value=72, value=29, step=1)
        OnlineSecurity = st.sidebar.selectbox("OnlineSecurity", ["Yes", "No", "No internet service"])
        OnlineBackup = st.sidebar.selectbox("OnlineBackup", ["Yes", "No", "No internet service"])
        InternetService = st.sidebar.selectbox("InternetService", ["DSL", "Fiber optic", "No"])
        DeviceProtection = st.sidebar.selectbox("DeviceProtection", ["Yes", "No", "No internet service"])
        TechSupport = st.sidebar.selectbox("TechSupport", ["Yes", "No", "No internet service"])
        Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.sidebar.radio("PaperlessBilling", ["Yes", "No"])
        MonthlyCharges = st.sidebar.number_input("MonthlyCharges", min_value=19, max_value=119, value=70, step=1)

        data = {
            "Dependents": Dependents,
            "tenure": tenure,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "InternetService": InternetService,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "MonthlyCharges": MonthlyCharges
        }
        return pd.DataFrame([data])

    df_Customer = input_user()
    st.subheader("Customer Feature Preview")
    st.write(df_Customer)

    # Load model
    try:
        model_loaded = pickle.load(open("model_gbc.sav", "rb"))
    except FileNotFoundError:
        st.error("❌ Model file not found!")
        st.stop()

    # Predict
    try:
        pred = model_loaded.predict(df_Customer)[0]
        if pred == 1:
            st.success("✅ **Pelanggan diprediksi BERHENTI (churn).**")
        else:
            st.info("🔒 **Pelanggan diprediksi TETAP berlangganan.**")
    except Exception as e:
        st.error(f"❌ Prediksi gagal: {e}")

# Sidebar navigasi utama
page = st.sidebar.selectbox("Pilih Halaman", ["Pendahuluan", "Penjelasan Fitur", "Prediksi Churn"])

if page == "Pendahuluan":
    show_pendahuluan()
elif page == "Penjelasan Fitur":
    show_feature_info()
elif page == "Prediksi Churn":
    show_prediction()
