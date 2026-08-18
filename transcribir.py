# import whisper
#
# model = whisper.load_model("turbo")
#
# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("CAPITULO3PARTE3.mp3")
# audio = whisper.pad_or_trim(audio)
#
# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)
#
# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")
#
# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)
#
# # print the recognized text
# print(result.text)


# import whisper

# Cargar modelo large-v3 (mejor para español)
# model = whisper.load_model("large-v3", device="cpu")
import torch
import whisper

if torch.cuda.is_available():
    device = "cuda"
    model_name = "turbo"
else:
    device = "cpu"
    model_name = "large-v3"

model = whisper.load_model(model_name, device=device)

# Transcribir directamente (¡automático todo!)
result = model.transcribe("unidad5parte1.mp3", language="es")

# Imprimir y guardar texto
texto = result["text"].strip()

print("TRANSCRIPCIÓN:")
print(texto)

# Guardar en TXT
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(texto)

print(f"\n✅ Guardado en: transcripcion.txt")
