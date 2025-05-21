# Telco-Customer-Churn-Prediction

## Latar Belakang
Manajemen Pemasaran sebuah perusahaan telekomunikasi menghadapi tantangan besar terkait tingkat churn pelanggan yang cukup tinggi dan mengalami kerugian sebesar $71,300. Mereka selama ini mengeluarkan biaya promosi ke seluruh pelanggan tanpa tahu siapa yang benar-benar berisiko berhenti menggunakan layanan. Strategi ini tidak efisien, karena sebagian besar promosi justru jatuh kepada pelanggan yang sebenarnya  tidak berniat berhenti berlangganan.

##  Rumusan Masalah 
Perusahaan belum memiliki sistem yang mampu memprediksi kemungkinan pelanggan akan berhenti berlangganan. Akibatnya, strategi promosi dilakukan secara massal ke seluruh pelanggan, yang mengakibatkan biaya promosi yang besar namun tidak efisien.

## Metric Evaluation
Cost FP: $100
Cost FN: $500

- False Positive (FP): Model memprediksi akan churn → beri promosi $100 Tapi kenyataannya pelanggan tidak akan churn → promosi tidak perlu → rugi $100
- False Negative (FN): Model memprediksi tidak akan churn → tidak beri promosi Tapi kenyataannya pelanggan churn → kehilangan pelanggan → rugi $500

Karena cost dari FN jauh lebih tinggi dibanding FP, karena itu F2-score dipilih sebagai metrik evaluasi utama.

## Tujuan Analisis
1. Memprediksi Churn Pelanggan berdasarkan data historis pelanggan.
2. Mengurangi Kerugian Finansial khususnya pelanggan (False Negative) yang memiliki dampak finansial besar dengan memberikan penanganan preventif.
3. Mengoptimalkan Strategi Promosi dengan hanya menargetkan pelanggan yang benar-benar berisiko tidak churn.
4. Menggunakan Metode Evaluasi yang Tepat Menggunakan metrik F2 
5. Memberikan Insight Fitur Penting yang paling berkontribusi terhadap keputusan churn agar perusahaan dapat melakukan intervensi bisnis yang lebih tepat sasaran

## Kondisi Data
- Data awal pada file data_telco_customer_churn.csv mempunyai 4930 rows.
- Data memiliki 11 kolom yang terdiri dari 10 kolom feature dan 1 kolom target, kolom target pada data ini adalah Churn.
- Tipe datanya 9 bertipe Kategorikal dan 2 bertipe Numerikal.
Perbandingan pelanggan yang Churn dan yang tidak Churn adalah 1288 : 3565

## Machine Learning Modeling
- Define X and y
- Data Splitting
- Data Preprocessing
- Hyperparameter Tuning dan CV
- Performance in Test Set
- Best Model
- Confusion Matrix
- Feature Importance

## Simulasi Prediksi Data Churn Untuk Manajer Pemasaran
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dp-machinelearning-kh.streamlit.app/)

## Kesimpulan
-	Tingkat Churn Pelanggan
Dari total data, sekitar 26,6% pelanggan melakukan churn. Ini menunjukkan bahwa lebih dari seperempat pelanggan memilih berhenti menggunakan layanan, yang merupakan sinyal kuat bagi manajemen untuk meningkatkan retensi pelanggan.
-	Pengaruh Fitur terhadap Churn
Berdasarkan feature importance dari model Gradient Boosting, fitur yang paling berpengaruh terhadap churn adalah:
    - tenure
    - MonthlyCharges
    - Contract
    - InternetService
-	Evaluasi Model Gradient Boosting
    -	F2 Score (Test Set) sebelum tuning: 0.71
    -	F2 Score (Test Set) sesudah tuning: 0.755
Artinya, tuning hyperparameter berhasil meningkatkan performa model dalam mengenali pelanggan yang benar-benar akan churn. Metrik F2 Score dipilih karena False Negative (kehilangan pelanggan) memiliki dampak biaya ($500) yang jauh lebih besar dibanding False Positive ($100).
-	Efisiensi Biaya Promosi
    - Tanpa ML, promosi diberikan ke seluruh pelanggan, menyebabkan biaya sia-sia sebesar $71,300.
    - Dengan ML, promosi menjadi lebih tepat sasaran dan kerugian turun menjadi $39,300.
    - Machine Learning berhasil menurunkan kerugian sampai 45% dari total kerugian sebelumnya
      
## Rekomendasi
-	Implementasikan Model Gradient Boosting ke Proses Operasional
Gunakan model ini dalam sistem pemasaran untuk memprioritaskan pelanggan berisiko tinggi churn agar mendapat perhatian khusus (diskon, insentif, komunikasi aktif).
-	Fokus pada Fitur Penting dan Pertimbangkan Penghapusan Fitur Kurang Relevan
Perusahaan dapat memusatkan analisis dan strategi pada pelanggan dengan:
    - Kontrak bulanan
    - Tenure pendek
    - Biaya bulanan tinggi
    - Jenis layanan internet tertentu (misalnya DSL atau Fiber)
-	Kembangkan Strategi Customer Retention
Berdasarkan hasil model, rancang strategi berbasis data untuk mengurangi churn, seperti:
   	- Penawaran kontrak tahunan
   	- Program loyalitas untuk pengguna baru
    - Paket bundling layanan internet dan telepon
-	Monitoring & Evaluasi Berkala
Model perlu dipantau dan ditingkatkan secara berkala untuk menyesuaikan dengan tren dan perilaku pelanggan yang dinamis.



