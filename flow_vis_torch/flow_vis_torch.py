from typing import Optional, Union

import torch


def flow_to_color(flow: torch.Tensor, clip_flow: Optional[Union[float, torch.Tensor]]) -> torch.Tensor:
    """
    Function converts a given optical flow map into the classical color schema.
    :param flow: (torch.Tensor) Optical flow tensor of the shape [batch size (optional), 2, height, width].
    :param clip_flow: (Optional[Union[float, torch.Tensor]]) Max value of flow values for clipping (default None).
    :return: (torch.Tensor) Flow visualization with the shape [batch size (if used), 3, height, width].
    """
    pass
