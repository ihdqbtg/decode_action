import base64, zlib, lzma, bz2, gzip

compressed_data = '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'

decompressed_data = zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode(compressed_data)))))
print(decompressed_data.decode())
