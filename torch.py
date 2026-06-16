import torch

# Rastgele devasa iki matris oluşturup kartın içinde çarpalım
x = torch.rand(10000, 10000).cuda()
y = torch.rand(10000, 10000).cuda()

print("Hesaplama basliyor...")
z = torch.matmul(x, y)
print("Hesaplama bitti, kart canavar gibi calisiyor!")
