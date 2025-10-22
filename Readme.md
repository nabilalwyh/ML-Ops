# Submission 1: Nama Proyek Anda
Nama: Nabila Alawiyah

Username dicoding: nabilaalawiyah

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Bank Customer Attrition Insights](https://www.kaggle.com/datasets/marusagar/bank-customer-attrition-insights) berisi data pelanggan bank dengan berbagai atribut seperti umur, skor kredit, saldo, status kartu, dan informasi aktivitas nasabah, serta kolom target Exited yang menunjukkan apakah pelanggan berhenti menjadi nasabah atau tidak. |
| Masalah | Bank perlu mengidentifikasi nasabah yang berpotensi meninggalkan layanan (churn), agar dapat melakukan tindakan pencegahan seperti penawaran promo atau peningkatan layanan. Saat ini, sulit bagi pihak bank untuk memprediksi churn secara manual karena jumlah data yang besar. |
| Solusi machine learning | Membangun model machine learning berbasis TensorFlow Extended (TFX) untuk memprediksi kemungkinan seorang nasabah akan churn (Exited = 1). Model ini akan membantu bank dalam mendeteksi nasabah berisiko tinggi secara otomatis dan lebih cepat. |
| Metode pengolahan | Data mentah diolah menggunakan komponen Transform dalam TFX. Proses ini mencakup pembersihan data, konversi tipe fitur numerik ke float32, fitur biner ke int64, dan penyesuaian nama kolom agar konsisten. Data kemudian dibagi menjadi 80% data training dan 20% data evaluasi menggunakan CsvExampleGen. |
| Arsitektur model | Model yang digunakan adalah Neural Network (Dense Neural Network) dengan beberapa lapisan Dense: 64 neuron (ReLU), 32 neuron (ReLU), dan lapisan output dengan 1 neuron (Sigmoid). Optimizer yang digunakan adalah Adam (learning rate 0.01) dengan loss function binary_crossentropy. |
| Metrik evaluasi | Model dievaluasi menggunakan metrik AUC, BinaryAccuracy, True/False Positives, dan True/False Negatives. Evaluasi dilakukan melalui komponen Evaluator menggunakan TensorFlow Model Analysis (TFMA). |
| Performa model | Berdasarkan hasil evaluasi menggunakan TensorFlow Model Analysis (TFMA), model menghasilkan nilai binary accuracy sebesar 0.7978, loss sebesar 0.5260, serta AUC sebesar 0.5783. Meskipun akurasi terlihat cukup tinggi, hasil evaluasi menunjukkan bahwa model cenderung hanya memprediksi kelas mayoritas (nasabah yang tidak keluar), yang ditunjukkan oleh nilai True Positive = 0 dan False Negative = 406. Hal ini mengindikasikan bahwa model belum mampu mendeteksi nasabah yang berpotensi churn dengan baik. |