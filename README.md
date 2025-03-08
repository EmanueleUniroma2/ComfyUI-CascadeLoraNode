# ComfyUI-CascadeLoraNode
A custom node to quickly apply multiple loras without need to add many load lora nodes:
![image](https://github.com/user-attachments/assets/4264f28b-1af5-411f-906c-e2bb23b4a712)


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

The node has a variable MAX_GROUPS that defines how many loras are supported, you can edit that number as you like.
