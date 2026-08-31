import pygame
import pygame._sdl2.audio as sdl2_audio
import time
import os

def play_on_device(device_name, sound_file='noteC.mp3'):
    """Инициализирует микшер с указанным устройством и проигрывает звук."""
    print(f"\nПробуем устройство: {device_name}")
    
    # Закрываем предыдущий микшер (если был)
    pygame.mixer.quit()
    
    try:
        # Инициализируем микшер с выбранным устройством
        # Можно задать частоту и другие параметры для совместимости
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512,
                          devicename=device_name)
    except Exception as e:
        print(f"  Ошибка инициализации микшера: {e}")
        return

    # Проверяем, существует ли файл
    if not os.path.isfile(sound_file):
        print(f"  Файл {sound_file} не найден в текущей папке!")
        return

    try:
        sound = pygame.mixer.Sound(sound_file)
    except pygame.error as e:
        print(f"  Ошибка загрузки звука: {e}")
        return

    # Устанавливаем громкость на максимум
    sound.set_volume(1.0)
    
    # Проигрываем один раз
    sound.play()
    print(f"  Играет... (длительность: {sound.get_length():.2f} сек)")
    
    # Ждём окончания воспроизведения
    while pygame.mixer.get_busy():
        pygame.time.delay(100)
    
    print(f"  Воспроизведение завершено на устройстве: {device_name}")

def main():
    # Инициализируем Pygame (обязательно для работы с аудио)
    pygame.init()
    
    # Получаем список устройств вывода (playback)
    try:
        devices = sdl2_audio.get_audio_device_names(False)
    except AttributeError:
        print("Ваша версия Pygame не поддерживает получение списка устройств.")
        print("Попробуйте обновить Pygame до версии 2.x.")
        pygame.quit()
        return

    if not devices:
        print("Нет доступных устройств вывода.")
        pygame.quit()
        return

    print(f"Найдено устройств для вывода: {len(devices)}")
    for i, dev in enumerate(devices, start=1):
        print(f"\n--- Тест {i} из {len(devices)} ---")
        play_on_device(dev)
        time.sleep(0.5)  # небольшая пауза между тестами

    print("\nВсе устройства протестированы.")
    pygame.quit()

if __name__ == "__main__":
    main()