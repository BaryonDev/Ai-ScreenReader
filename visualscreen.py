import asyncio
import websockets
import json
import numpy as np
import pyautogui
import base64
import cv2
import requests
import io

class VisualScreenReader:
    def __init__(self, ollama_endpoint="http://localhost:11434/api/generate"):
        self.ollama_endpoint = ollama_endpoint
        self.running = False

    def image_to_base64(self, image):
        if isinstance(image, np.ndarray):
            if image.shape[2] == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            _, buffer = cv2.imencode('.png', image)
            return base64.b64encode(buffer).decode('utf-8')
        return None

    def process_screen_image(self, image, text_prompt=None):
        base64_image = self.image_to_base64(image)
        if not base64_image:
            return "Gagal memproses gambar"
        prompt = text_prompt or "Jelaskan apa yang ada di gambar ini secara detail"
        payload = {
            "model": "minicpm-v",
            "prompt": prompt,
            "images": [base64_image],
            "stream": False
        }
        try:
            response = requests.post(
                self.ollama_endpoint, 
                json=payload, 
                headers={'Content-Type': 'application/json'}
            )
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'Tidak ada deskripsi')
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Kesalahan: {str(e)}"

    async def websocket_server(self, websocket, path=None):
        try:
            async for message in websocket:
                data = json.loads(message)
                if data['type'] == 'screen_selection':
                    selection = data['data']
                    screenshot = pyautogui.screenshot(region=(
                        selection['x'], 
                        selection['y'], 
                        selection['width'], 
                        selection['height']
                    ))
                    screenshot_array = np.array(screenshot)
                    text_prompt = data.get('prompt', None)
                    description = self.process_screen_image(
                        screenshot_array, 
                        text_prompt
                    )
                    await websocket.send(json.dumps({
                        'type': 'screen_description',
                        'description': description
                    }))
                elif data['type'] == 'text_input':
                    text = data.get('text', '')
                    screenshot = pyautogui.screenshot()
                    screenshot_array = np.array(screenshot)
                    description = self.process_screen_image(
                        screenshot_array, 
                        text
                    )
                    await websocket.send(json.dumps({
                        'type': 'text_description',
                        'description': description
                    }))
        except websockets.exceptions.ConnectionClosed:
            print("Koneksi WebSocket ditutup")
        except Exception as e:
            print(f"Kesalahan pada websocket_server: {e}")

    async def start_websocket_server(self):
        server = await websockets.serve(
            self.websocket_server, 
            "localhost", 
            8765
        )
        await server.wait_closed()

    async def start(self):
        self.running = True
        await self.start_websocket_server()

def main():
    screen_reader = VisualScreenReader()
    asyncio.run(screen_reader.start())

if __name__ == "__main__":
    main()
