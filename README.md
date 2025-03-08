# ComfyUI-CascadeLoraNode
A custom node to quickly apply many loras without need to add many nodes
This is way easier to integrate into your comfy install by a quick manual copy-paste.

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

Then manually add the content of the file on top (or anywhere you like) of the nodes.py files inside your comfyUI root.
