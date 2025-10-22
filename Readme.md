# Submission 1: Nama Proyek Anda
Nama: Nabila Alawiyah

Username dicoding: nabilaalawiyah

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Bank Customer Attrition Insights](https://www.kaggle.com/datasets/marusagar/bank-customer-attrition-insights) |
| Masalah | Bank perlu mengidentifikasi nasabah yang berpotensi meninggalkan layanan (churn), agar dapat melakukan tindakan pencegahan seperti penawaran promo atau peningkatan layanan. Saat ini, sulit bagi pihak bank untuk memprediksi churn secara manual karena jumlah data yang besar. |
| Solusi machine learning | Membangun model machine learning berbasis TensorFlow Extended (TFX) untuk memprediksi kemungkinan seorang nasabah akan churn (Exited = 1). Model ini akan membantu bank dalam mendeteksi nasabah berisiko tinggi secara otomatis dan lebih cepat. |
| Metode pengolahan | Data mentah diolah menggunakan komponen Transform dalam TFX. Proses ini mencakup pembersihan data, konversi tipe fitur numerik ke float32, fitur biner ke int64, dan penyesuaian nama kolom agar konsisten. Data kemudian dibagi menjadi 80% data training dan 20% data evaluasi menggunakan CsvExampleGen. |
| Arsitektur model | Model yang digunakan adalah Neural Network (Dense Neural Network) dengan beberapa lapisan Dense: 64 neuron (ReLU), 32 neuron (ReLU), dan lapisan output dengan 1 neuron (Sigmoid). Optimizer yang digunakan adalah Adam (learning rate 0.01) dengan loss function binary_crossentropy. |
| Metrik evaluasi | Model dievaluasi menggunakan metrik AUC, BinaryAccuracy, True/False Positives, dan True/False Negatives. Evaluasi dilakukan melalui komponen Evaluator menggunakan TensorFlow Model Analysis (TFMA). |
| Performa model | Model mencapai akurasi sekitar 85% dan AUC lebih dari 0.80, yang menunjukkan kemampuan model yang baik dalam membedakan nasabah yang akan churn dan yang tidak. Hasil evaluasi menunjukkan model baru memenuhi ambang batas (threshold) dan diberkati untuk dipush ke direktori serving. |