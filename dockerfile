# Docker imajınızı temel alacağınız taban imajı belirleyin
FROM python:3.10.12

# Uygulamanızın çalışacağı çalışma dizinini belirleyin
WORKDIR /home/aisankheiri/Desktop/acikkaynakodev

# Uygulama bağımlılıklarını kopyalayın
COPY requirements.txt .

# Bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayın
COPY . .

# Konteynerin hangi portu dinleyeceğini belirleyin
EXPOSE 5000

# Uygulamayı başlatmak için komutu belirleyin
CMD [ "python", "app.py" ]
