#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script for cropping the largest square region from an image.
"""

import os
from PIL import Image, ImageOps


THUMB_WIDTH = 200
IMAGE_FOLDER = './original_images/'
SQUARE_FOLDER = './thumbnails_squares/'


def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    cropped_img = img.crop((
        (img_width - crop_width) // 2,
        (img_height - crop_height) // 2,
        (img_width + crop_width) // 2,
        (img_height + crop_height) // 2
    ))
    return cropped_img


def crop_max_square(img):
    """
    Image.size returns the width and height of an image, and the smallest
    value out of these is used as the length of the square to be cropped.
    """
    max_square = crop_center(img, min(img.size), min(img.size))
    return max_square


def main():
    for image in os.listdir(IMAGE_FOLDER):
        # Get the filename and the extension for the image file (used later when saving)
        filename, ext = os.path.splitext(image)
        # Open the image and get a pillow Image object
        raw_im = Image.open(IMAGE_FOLDER + image)
        # Ensure the orientaion of the image is correct according to its EXIF data
        corrected_im = ImageOps.exif_transpose(raw_im)
        # Get the largest possible square from the centre of the image
        im_square = crop_max_square(corrected_im)
        # Resize the square to the desired size (LANCZOS is the antialias filter)
        im_resized = im_square.resize((THUMB_WIDTH, THUMB_WIDTH), Image.LANCZOS)
        # Save the resized square with reduced quality
        im_resized.save(SQUARE_FOLDER + filename + "_square" + ext, quality=75)    


if __name__ == '__main__':
    main() 
