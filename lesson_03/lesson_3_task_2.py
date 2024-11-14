from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "200 Pro", "+79084567890"),
    Smartphone("Huawei", "Mate 50", "+79168789574"),
    Smartphone("Samsung", "Galaxy Z", "+79257308770"),
    Smartphone("IPhone", "16 Pro Max", "+79772041938"),
    Smartphone("Xiaomi", "12 Lite", "+79186522255")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}") 