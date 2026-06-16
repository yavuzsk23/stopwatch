import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def ses_analiz_et(dosya_yolu):
    print(f"🎵 {dosya_yolu} dosyası analiz ediliyor...")

    try:
        # 1. Ses dosyasını yüklüyoruz
        y, sr = librosa.load(dosya_yolu)

        # 2. Sesin Tempo (BPM) değerini buluyoruz
        # Librosa güncel sürümlerinde 'tempo' bir array (dizi) olarak döner
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        
        # Dizinin ilk elemanını alarak scalar hatasını çözüyoruz
        # [0] ekleyerek listenin içindeki gerçek sayıyı çekiyoruz
        gercek_bpm = float(tempo[0]) if isinstance(tempo, (np.ndarray, list)) else float(tempo)
        
        print(f"🥁 Tahmini Tempo: {gercek_bpm:.2f} BPM")

        # 3. Görselleştirme
        plt.figure(figsize=(10, 4))
        plt.title("CYBERIA AUDIO WAVEFORM")
        librosa.display.waveshow(y, sr=sr, color='cyan') # Rengi Cyberia mavisi yaptık
        plt.xlabel("Zaman (Saniye)")
        plt.ylabel("Genlik")
        
        print("📈 Ses dalgası (Waveform) grafiği hazırlanıyor...")
        plt.show()

    except Exception as e:
        print(f"Kanka teknik bir arıza: {e}")

# Dosyanın adından emin ol kanka, E: diskindeyse tam yolunu yazabilirsin
ses_analiz_et("test_ses.wav")
