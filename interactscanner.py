from scapy.all import ARP, Ether, srp
import ipaddress

def scan_local_network(ip_range):
    try:
        # Создаем ARP запрос для сканирования с указанным диапазоном IP адресов
        arp = ARP(pdst=ip_range)
        # Создаем Ethernet фрейм
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # Комбинируем ARP запрос и Ethernet фрейм
        packet = ether/arp
        # Отправляем пакет и получаем ответы
        result = srp(packet, timeout=3, verbose=False)[0]

        # Создаем список активных IP адресов
        active_ips = []
        for sent, received in result:
            active_ips.append(received.psrc)

        return active_ips
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def main():
    print("Программа для сканирования локальной сети")
    print("Введите диапазон IP адресов для сканирования (например, 192.168.1.1/24):")
    ip_range = input("Диапазон IP адресов: ")

    try:
        # Проверяем введенный диапазон IP адресов
        ip_network = ipaddress.ip_network(ip_range)
        if ip_network.version != 4:
            print("Поддерживаются только IPv4 адреса.")
            return

        # Сканируем локальную сеть
        active_ips = scan_local_network(str(ip_network))
        
        # Выводим список активных IP адресов
        print("\nАктивные IP адреса в указанном диапазоне:")
        for ip in active_ips:
            print(ip)
    except ValueError:
        print("Неверный формат IP адреса или диапазона.")

if __name__ == "__main__":
    main()
