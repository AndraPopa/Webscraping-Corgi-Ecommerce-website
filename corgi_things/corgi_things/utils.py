def get_image_link(sequence: str):
    image_link = sequence.split('content')[1].lstrip('="//').rstrip('">')
    return image_link
