# Handy Scripts for Fiji
Hi there! These are just some handy tools for Fiji to take care of typical day to day tasks around the lab. A description for each script and how to use it can be found in this README document. Installation instructions are also provided. Eventually, I will create an update site for the tools, but for now its still pretty easy to install everything manually. If you notice any errors or ways the scripts could be improved, [open an issue](https://github.com/ScienceToolkit/imagej-utilities/issues). If you have modified them and think the changes you have made are general improvements that should be incorporated, feel free to make a [pull request](https://yangsu.github.io/pull-request-tutorial/).

## Installation
To install, download the most recent release of the utilities from the [releases page](https://github.com/ScienceToolkit/imagej-utilities/releases). Then you can create a custom place to keep them that is handy for you. Here's how to do it:
1. Unpack the compressed release archive you downloaded. It doesn't matter where.
2. Navigate your way into the _scripts_ folder in the imagej-utilities folder that was unpacked.
3. Highlight all of the folders in this directory and copy them.
4. Now we need to put them into our Fiji installation so they [show up] in the GUI. We can put them in a custom drop down menu, which we will call "My Tools". To do this make a folder in the _.../fiji.app/plugins/Scripts_ folder titled "My_Tools".
5. Now paste the files into _.../fiji.app/plugins/Scripts/My_Tools_ and they will show up on a custom drop down menu on the Fiji interface!

## DPI Dialog
The DPI Dialog tool is meant to make quick work of adjusting images for journals specifications. It uses __ONLY__ nearest neighbour interpolation to avoid unfaithfully smoothing images (microscopy in mind here). To use it, follow the directions below.

1. Open an image the image you wish to render.
2. Set either the width or height to the specification required. One of these should be left as 0. The one that is left as 0 will be automatically calculated using the aspect ratio of the open image.
3. Set the DPI to the specification required. This is typically 300 dots per inch, so that is the default.
4. Click OK and you are all done! :rocket:
