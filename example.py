import torch
import numpy as np
import torchvision
import flow_vis
import flow_vis_torch


def load_flo_file(file_path: str) -> torch.Tensor:
    """
    Function loads a .flo file.
    :param file_path: (str) Path to flo file
    :return: (torch.Tensor) Torch.Tensor of the shape [2, height, width]
    """
    # Open file
    with open(file_path, "rb") as file:
        # Load date
        data_array: np.ndarray = np.fromfile(file, np.float32)[3:]
        # Reshape data
        flow: np.ndarray = data_array.reshape((436, 1024, 2))
    # To PyTorch and reshape
    return torch.from_numpy(flow).permute(2, 0, 1)


if __name__ == '__main__':
    for file in ["frame_0014.flo", "frame_0005.flo", "frame_0023.flo"]:
        # Load flow maps
        flow = load_flo_file(file_path=file)
        # Standard package
        flow_rgb_flow_vis = torch.from_numpy(
            flow_vis.flow_to_color(flow.clone().permute(1, 2, 0).numpy()).astype(float)).permute(2, 0, 1)
        torchvision.utils.save_image(flow_rgb_flow_vis.float(), file.replace(".flo", "_flow_vis.png"), normalize=True)
        # PyTorch version
        flow_rgb_flow_vis_torch = flow_vis_torch.flow_to_color(flow)
        torchvision.utils.save_image(flow_rgb_flow_vis.float(), file.replace(".flo", "_flow_vis_torch.png"),
                                     normalize=True)
