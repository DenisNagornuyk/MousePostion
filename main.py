from pynput import mouse
#обробка координат курсора
def on_move(x, y):
	print(f"Position: x:{x}, y:{y}")

#обробка натиснення
def on_click(x, y, button, pressed):
	pressed_status = 'Pressed' if pressed else 'Released'
	print(f"Position: x:{x}, y:{y} | Status in pressing: {pressed_status} | button: {button}")

#збираємо подію поки не закінчется поток
with mouse.Listener(
		on_move=on_move,
		on_click=on_click) as listener:
	listener.join()

#метож для відстеження миші
listener = mouse.Listener(
	on_move=on_move,
	on_click=on_click)
listener.start()