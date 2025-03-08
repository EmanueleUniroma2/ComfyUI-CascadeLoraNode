# ComfyUI-CascadeLoraNode
A custom node to quickly apply many loras without need to add many load lora nodes:
![image](https://github.com/user-attachments/assets/40a39c3b-b829-41c3-bfc0-dcc40b6057c7)


# How to install
Just add these to the declarations in your comfy ui nodes.py

NODE_CLASS_MAPPINGS = {
  ...,
  "LoraCascadeModelApplyNode": LoraCascadeModelApplyNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
  ...,
  "LoraCascadeModelApplyNode": "Lora Cascade Model Apply",
}

Then manually add the content of **LoraCascadeModelApplyNode.py** the file on top (or anywhere you like) of the nodes.py files inside your comfyUI root.
