import base64


def text_to_base64(text):
    return base64.b64encode(text.encode()).decode()


def base64_to_text(text):
    return base64.b64decode(text).decode()


def text_to_bin(text):
    return " ".join([bin(ord(i))[2:] for i in text])


def bin_to_text(text):
    return "".join([chr(int(i, 2)) for i in text.split(" ")])


coders = {"text_to_base64": text_to_base64,
          "base64_to_text": base64_to_text,
          "text_to_bin": text_to_bin,
          "bin_to_text": bin_to_text}


def do_pipeline(text, pipeline):
    pipeline_coders = pipeline.split(" | ")
    for coder_name in pipeline_coders:
        if coder_name in coders:
            try:
                text = coders[coder_name](text)
            except Exception as ex:
                text = "ERROR: " + str(ex)
                break
    return text
