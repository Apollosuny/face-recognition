import tensorflow as tf


def preprocess(file_path):

    # Read in image from file path
    byte_img = tf.io.read_file(file_path)
    # Load in the image
    img = tf.io.decode_jpeg(byte_img)

    # Preprocessing steps - resizing the image to be 100x100x3
    img = tf.image.resize(img, (100, 100))
    # Scale image to be between 0 and 1
    img = img / 255.0

    # Return image
    return img


def draw_ped(
    self, img, label, x0, y0, xt, yt, color=(255, 127, 0), text_color=(255, 255, 255)
):

    (w, h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(img, (x0, y0 + baseline), (max(xt, x0 + w), yt), color, 2)
    cv2.rectangle(img, (x0, y0 - h), (x0 + w, y0 + baseline), color, -1)
    cv2.putText(
        img, label, (x0, y0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA
    )
    return img
