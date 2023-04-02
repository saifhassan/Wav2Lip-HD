import gdown

######### downloading models ########

urls = {
    "wav2lip_gan.pth": "10Iu05Modfti3pDbxCFPnofmfVlbkvrCm", 
    "face_segmentation.pth": "154JgKpzCPW82qINcVieuPH3fZ2e0P812",
    "esrgan_yunying.pth": "1aB-jqBikcZPJnFrJXWUEpvF2RFCuerSe",
    "pretrained.state": "1_MGeOLdARWHylC1PCU2p5_FQztD4Bo7B"
}

for name, id in urls.items():
    url = f"https://drive.google.com/uc?id={id}"
    output = f"checkpoints/{name}"
    gdown.download(url, output, quiet=False)
    print(f"Loaded {name}")

######### downloading videos ########
# If you load files from Drive, run this cell

# Paste the filename and Google Drive ID of your video below.
urls = {
    "yunying_30s.mp4": "1dggydm07RHrxiFUIH_51RXmkMcD_bMPE",
}

for name, id in urls.items():
    url = f"https://drive.google.com/uc?id={id}"
    output = f"videos/{name}"
    gdown.download(url, output, quiet=False)
    print(f"Loaded {name}")