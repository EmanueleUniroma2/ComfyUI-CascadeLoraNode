# copy paste this into your ypur nodes.py inside the comfyUi root
class LoraCascadeModelApplyNode:
    MAX_GROUPS = 6

    @classmethod
    def INPUT_TYPES(cls):
        inputs = {"required": {}}
        # Always need a checkpoint input
        inputs["required"]["ckpt_name"] = (
            folder_paths.get_filename_list("checkpoints"),
            {
                "tooltip": "The name of the checkpoint (model) to load."
            }
        )
        
        # Define a fixed maximum number of LoRA groups
        for i in range(cls.MAX_GROUPS):
            # Each group has two inputs: a lora file selector and a weight.
            lora_key = f"lora_{i}"
            model_weight_key = f"weight_{i}"
            model_enabled_key = f"enabled_{i}"

            inputs["required"][lora_key] = (
                folder_paths.get_filename_list("loras"),
                {
                    "default": "",
                    "tooltip": f"Select a LoRA. Leave empty to finish adding LoRAs."
                })

            inputs["required"][model_weight_key] = (
                "FLOAT",
                {"default": 1, "min": 0.0, "max": 2.0, "step":0.1, "round": 0.01, "tooltip": f"Clip and Model weight for lora {i}."}
            )

            inputs["required"][model_enabled_key] = (
                "BOOLEAN",
                {"default": i == 0, "tooltip": f"Determ if lora {i} will be applied."}
            )
        return inputs

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    OUTPUT_TOOLTIPS = (
        "The diffusion model with cascaded LoRA modifications.",
        "The CLIP model with cascaded LoRA modifications.",
        "The VAE from the checkpoint."
    )
    FUNCTION = "load_checkpoint_and_apply_loras"
    CATEGORY = "loaders"
    DESCRIPTION = (
        "Loads a diffusion model checkpoint and applies multiple LoRA modifications in cascade. "
        "For each LoRA group, a LoRA file is selected and a weight is provided (used for both the model and CLIP). "
        "Processing stops when a LoRA selector is left empty."
    )

    def load_checkpoint_and_apply_loras(self, **kwargs):
        # Load the checkpoint (model, clip, and VAE)
        ckpt_name = kwargs.get("ckpt_name")
        ckpt_path = folder_paths.get_full_path_or_raise("checkpoints", ckpt_name)
        checkpoint_out = comfy.sd.load_checkpoint_guess_config(
            ckpt_path,
            output_vae=True,
            output_clip=True,
            embedding_directory=folder_paths.get_folder_paths("embeddings")
        )
        model, clip, vae = checkpoint_out[:3]

        # Iterate over the LoRA groups until an empty LoRA selector is encountered.
        i = 0
        while i < self.__class__.MAX_GROUPS:
            lora_key = f"lora_{i}"
            weight_key = f"weight_{i}"
            enabled_key = f"enabled_{i}"

            if enabled_key:
                lora_name = kwargs[lora_key]
                # Retrieve the weight for this group.
                model_weight = kwargs.get(weight_key, 1.0)
                clip_weight = kwargs.get(weight_key, 1.0)

                # Resolve the full path and load the LoRA file.
                lora_path = folder_paths.get_full_path_or_raise("loras", lora_name)
                lora = comfy.utils.load_torch_file(lora_path, safe_load=True)

                # Apply the LoRA to both the diffusion (model) and CLIP models.
                model, clip = comfy.sd.load_lora_for_models(model, clip, lora, model_weight, clip_weight)

            i += 1

        return (model, clip, vae)
