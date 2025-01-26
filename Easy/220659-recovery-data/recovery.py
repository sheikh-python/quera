def data_recovery(data):
    head_dict = {
        b'\x89PNG\r\n\x1a\n':'PNG',
        b'\xff\xd8\xff':'JPEG',
        b'\x42\x4d':'BMP',
        b'\x49\x49\x2a\x00':'TIFF',
        b'\x47\x49\x46\x38':'GIF',
        b'\x50\x4b\x03\x04':'ZIP',
        b'\x7fELF' :'ELF',
        b'\x25\x50\x44\x46':'PDF',
        b'\x49\x44\x33':'MP3',
        b'\xff\xfb':'MPEG',
        b'\x00\x00\x01\x00':'PDDF',
        b'\x00\x01\x00\x00':'ICO' 
    }
    list_of_file = []
    
    for i in head_dict.keys():
        if i in data:
            list_of_file.append(head_dict[i])
            
    return(list_of_file)
            
        


