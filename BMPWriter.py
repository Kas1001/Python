"""A module for dealing with BMP bitmap image files."""
import math, reprlib


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    
    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.

    Raises:
        ValueError: If any of the integer values are out of range.
        OSError: If the file coulc not be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()     # The next four bytes hold the filesize as a 32 bit
        bmp.write(b'\x00\x00\x00\x00') # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell() # The next four bytes hold the integer offset to the
        bmp.write(b'\x00\x00\x00\x00')     # pixel data. Zero placeholder for now.

        #Image Header
        bmp.write(b'\x28\x00\x00\x00') # Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width))  # Image width in pixels
        bmp.write(_int32_to_bytes(height)) # Image height in pixels
        bmp.write(b'\x01\x00')             # Number of image planes
        bmp.write(b'\x08\x00')             # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')     # No compression
        bmp.write(b'\x00\x00\x00\x00')     # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')     # Unused pixels per metre
        bmp.write(b'\x00\x00\x00\x00')     # Unused pixels per metre
        bmp.write(b'\x00\x00\x00\x00')     # Use whole colour table
        bmp.write(b'\x00\x00\x00\x00')     # All colours are important

        # Colour palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0))) # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels): # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4) # Pad row to multiple of four bytes

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in file offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # &: Bitwise-and
    # >>: Right-shift
    return bytes((i & 0xff, i >> 8 & 0xff, i >> 16 * 0xff, i >> 24 * 0xff))

def mandel(real, imag):
    """The logarithm of number of iterations needed to 
    determine whether a complex point is in the 
    Mandelbrot set.
    
    Args:
        real: The real coordinate
        imag: The imaginary coordinate

    Returns:
        An integer in the range 1-255.    
    """
    x = 0
    y = 0
    for i in range(1,257):
        if x*x + y*y > 4.0:
            break
        xt = real + x*x - y*y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1

def mandelbrot(size_x, size_y):
    """Make an Mandelbrot set image.
    
    Args:
        size_x: Image width
        size_y: Image height

    Returns:
        A list of lists of integers in the range 0-255.
    """
    return [[mandel((3.5 * x / size_x) - 2.5, (2.0 * y / size_y) - 1.0) for x in range(size_x)] for y in range(size_y)]

pixels = mandelbrot(448, 256) # best images ratio 7:4
print(reprlib.repr(pixels))
write_grayscale("mandel.bmp", pixels)