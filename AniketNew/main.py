from gradio_client import Client, handle_file
import os
import io
import shutil
import sys

# Force UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


client = Client("levihsu/OOTDiffusion")
result = client.predict(
		vton_img=handle_file('C:/Users/Admin/Desktop/standingman2.png'),
		#garm_img=handle_file('https://assets.ajio.com/medias/sys_master/root/20231101/YoG0/65427d7dafa4cf41f56dda0d/-473Wx593H-466764378-lavender-MODEL.jpg'),
        garm_img=handle_file('C:/Users/Admin/Desktop/HackerRamp/AniketNew/ClothInputs/8f80ce39-c8f0-49cc-858f-47107fdef543.png'),
		n_samples=1,
		n_steps=20,
		image_scale=2,
		seed=-1,
		api_name="/process_hd"
)
print(result)

# Extract the path of the generated image from the result
temp_image_path = result[0]['image']

# Define the destination path
destination_image_path = '../Myntra/Frontend/src/assets/ModelImages/ansh_8f80ce39-c8f0-49cc-858f-47107fdef543.webp'

# Create directories if they don't exist
os.makedirs(os.path.dirname(destination_image_path), exist_ok=True)

# Copy the image to the destination
shutil.copy(temp_image_path, destination_image_path)

print("Image saved successfully at", destination_image_path)
