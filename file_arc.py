try:
  import hashlib
  import struct
except (ImportError, ModuleNotFoundError) as err:
  print('err_message: {}'.format(err))


  

PKG_HDR_FT = '8sI8sI'
PKG_HDR_SZ = struct.calcsize(PKG_HDR_FT)
FHR_BLK_FT = '32sII64s'
FHR_BLK_SZ = struct.calcsize(FHR_BLK_FT)


iobt = lambda x: bytearray(x, 'ascii')  

class FileArc:
  @staticmethod
  def GetHeaderInfo(src: str):
    with open(src, 'rb') as iFile:
      hdr_str = iFile.read(PKG_HDR_SZ)
      vlx = struct.unpack(PKG_HDR_FT, hdr_str)
      hdr_col = []
      remain = vlx[3]
      while remain:
        hdr_col += [struct.unpack(FHR_BLK_FT, iFile.read(FHR_BLK_SZ))]
        remain -= 1
      print(vlx)
      for elm in hdr_col:
        hasher = hashlib.sha256()
        iFile.seek(elm[2], 0)
        fsz = elm[1]
        read_size = min(fsz ,4096)
        for chunk in iter(lambda: iFile.read(read_size), b''):
          hasher.update(chunk)
          print(len(chunk))
          read_size = max(min(fsz - read_size ,4096), 0)
        print(elm)
        print(hasher.hexdigest())
        
  @staticmethod
  def Create(sink: str, *source):
    ahdr = {
      'magic':'special', 
      'version': 1, 
      'options':'nz', 
      'files': 0
    }
    fhdr = []
    def WritePHDR(sink_dst):
      try:
        sink_dst.seek(0, 0) # write to the beginning of the file
        vl = struct.pack(PKG_HDR_FT,
                         iobt(ahdr['magic']), 
                         ahdr['version'], 
                         iobt(ahdr['options']), 
                         ahdr['files'])
        print('size', len(vl))
        sink_dst.write(vl)
      except Exception as e:
        print(e)
    def HeaderAsBin(ihdr):
      ENCODE_FMT = ''
      fn, sz, dl, hsh = ihdr.values()
      return struct.pack(FHR_BLK_FT,iobt(fn) , dl, sz, iobt(hsh))
    def ContructHeader(fname):
      'hashlib.sha256()'
      fsz = 0
      hasher = hashlib.sha256()
      with open(fname, 'rb') as iFileHDR:
        iFileHDR.seek(0, 2) # Seek the end of the file
        fsz = iFileHDR.tell() # Get current position of file
        iFileHDR.seek(0, 0) # Seek the begin of the file
        for chunk in iter(lambda: iFileHDR.read(4096), b''):
          hasher.update(chunk)
      print(hasher.hexdigest(), len(str(hasher.hexdigest())))
      return {'name':fname, 'size': fsz, 'dloc': 0, 'hash': hasher.hexdigest()}
    for src in source:
      fhdr += [ContructHeader(src)]
    ahdr['files'] = len(fhdr)

    with open(sink, 'wb') as oFile:
      WritePHDR(oFile)
      for fsr in fhdr:
        vdr = HeaderAsBin(fsr)
        print(len(vdr))
        oFile.write(vdr)
      for i, src in enumerate(source):
        with open(src, 'rb') as iFile:
          fhdr[i]['dloc'] = oFile.tell() # Write current position of file
          for chunk in iter(lambda: iFile.read(4096), b''):
              oFile.write(chunk)
      oFile.seek(0, 0)
      WritePHDR(oFile)
      for fsr in fhdr:
        vdr = HeaderAsBin(fsr)
        print(vdr)
        oFile.write(vdr)
    print('complete')

    
if __name__ == '__main__':
  FileArc.Create('result.bin','curse.py','newish.py','basic.py')
  FileArc.GetHeaderInfo('result.bin')
