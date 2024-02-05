# importing os module
import os
import base64

# Function to rename multiple files
def main():
    
    WriteFile = "C:/Users/Andrew/Documents/Work/EHS - Discard Process"
    
    type = os.listdir(WriteFile)
    
    for i in type:
        Data = []
        path = WriteFile+"/"+i
        for j in os.listdir(path):
            textfile = open(path+"/Strings.txt",'w')
            with open(path+"/"+j, 'rb') as image_file:
                base64_bytes = base64.b64encode(image_file.read())
                base64_string = base64_bytes.decode()
                FileName = "fileName: "+j
                FileString = "Base 64 String: "+base64_string
                Data.append([FileName,FileString])
            textfile.write(str(Data))
            textfile.close()
                

            

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()

