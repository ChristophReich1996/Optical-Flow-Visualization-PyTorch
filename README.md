# Optical Flow Visualization for PyTorch

This repository is a PyTorch fork of the [OpticalFlow_Visualization](https://github.com/tomrunia/OpticalFlow_Visualization) (flow_vis) repository, originally published under the [MIT license](https://github.com/tomrunia/OpticalFlow_Visualization/blob/master/LICENSE.txt). The optical flow visualization follows the color encoding proposed in the paper "[A database and evaluation methodology for optical flow](https://link.springer.com/content/pdf/10.1007/s11263-010-0390-2.pdf)" by Baker et al. published at ICCV 2007 [1].

## Installation

Simply run the following command to install `flow_vis_torch`.

```shell script
pip install git+https://github.com/ChristophReich1996/Optical-Flow-Visualization-PyTorch
```

## Usage

Convert a given flow of the shape `(batch size (optional), 2, height, width)` to an RGB image of the shape `(batch size (optional), 3, height, width)` by calling `flow_vis_torch.flow_to_color`.

```python
import flow_vis_torch
flow_rgb = flow_vis_torch.flow_to_color(flow)
```

For a detailed example have a look at the [example script](example.py).

## Visualizations

Flow maps taken from the [MPI Sintel Flow Dataset](http://sintel.is.tue.mpg.de/) [2].

<table>
  <tr>
    <td> Output flow_vis_torch </td>
    <td> Output <a href="https://github.com/tomrunia/OpticalFlow_Visualization">flow_vis</a> </td>
  </tr> 
  <tr>
    <td> <img src="/images/frame_0005_flow_vis_torch.png"  alt="1" width = 256px height = 109px > </td>
    <td> <img src="/images/frame_0005_flow_vis.png" alt="2" width = 256px height = 109px> </td>
  </tr>
  <tr>
    <td> <img src="/images/frame_0014_flow_vis_torch.png"  alt="3" width = 256px height = 109px > </td>
    <td> <img src="/images/frame_0014_flow_vis.png" alt="4" width = 256px height = 109px> </td>
  </tr>
  <tr>
    <td> <img src="/images/frame_0023_flow_vis_torch.png"  alt="5" width = 256px height = 109px > </td>
    <td> <img src="/images/frame_0023_flow_vis.png" alt="6" width = 256px height = 109px> </td>
  </tr>
</table>

## References

```bibtex
[1] @inproceedings{Baker2007,
        title={{A Database and Evaluation Methodology for Optical Flow}},
        author={Baker, Simon and Roth, Stefan and Scharstein, Daniel and Black, Michael J and Lewis, JP and Szeliski, Richard},
        booktitle={{International Conference on Computer Vision (ICCV)}},
        pages={1--8},
        year={2007},
        organization={IEEE}
}
```

```bibtex
[2] @inproceedings{Butler2012,
        title={{A Naturalistic Open Source Movie for Optical Flow Evaluation}},
        author={Butler, Daniel J and Wulff, Jonas and Stanley, Garrett B and Black, Michael J},
        booktitle={{European Conference on Computer Vision (ECCV)}},
        pages = {611--625},
        year = {2012},
        publisher={Springer}
}
```