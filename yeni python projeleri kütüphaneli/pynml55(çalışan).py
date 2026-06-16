import subprocess

def get_gpu_status_direct():
    try:
        # NVIDIA-SMI aracına direkt soruyoruz
        # query-gpu: Sıcaklık ve Bellek kullanımını istiyoruz
        command = "nvidia-smi --query-gpu=temperature.gpu,memory.used,memory.total --format=csv,noheader,nounits"
        result = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        
        # Çıktıyı parçalara ayırıyoruz
        temp, used_mem, total_mem = result.split(', ')
        
        print(f"--- CYBERIA GPU MONITOR (Direct) ---")
        print(f"GPU Sıcaklık: {temp}°C")
        print(f"VRAM Kullanımı: {used_mem} MB / {total_mem} MB")
        
        # Eğer sıcaklık 75'ten fazlaysa uyar
        if int(temp) > 75:
            print("⚠️ DİKKAT: Ekran kartı ısınıyor, fanları kontrol et!")
            
    except Exception as e:
        print(f"Hala bir sorun var kanka: {e}")
        print("İpucu: NVIDIA sürücülerinin yüklü olduğundan emin ol.")

if __name__ == "__main__":
    get_gpu_status_direct()
