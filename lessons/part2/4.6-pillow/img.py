from PIL import Image

def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    with Image.open(in_path) as im:
        new_img = im.crop((10, 50, 100, 60)).resize((im.width * 2, im.height * 2))
        new_img.save(out_path)
    
if __name__=='__main__':
    print(generate_postcard('./imgs/img.jpg', "./imgs/img-modified.jpg"))

