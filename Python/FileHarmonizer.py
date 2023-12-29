# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

	type = os.listdir("[INSERT DRIVE LOCATION HERE]")

	for i in type:  
            # Ignore Audio Conditional
            if i != "Audio":
                
                # Establish Directory
                folder = "[INSERT DRIVE LOCATION HERE]{}".format(i)
                
                # loop over every file in each listed directory
                for count, filename in enumerate(os.listdir(folder)):

                    OldExtension = filename.split('.')[-1]

                    # conditional to keep extension except for certain cases
                    if OldExtension == "png" or OldExtension == "jpeg" or OldExtension == "jpg":
                        extension = "png"
                    elif OldExtension == "mp4" or OldExtension == "webm":
                        extension = "mp4"
                    else:
                        extension = OldExtension

                    if filename.split(' ')[0] != i:
                        # Rename File Process   
                        dst = f"{i} {str(len(os.listdir(folder))+count)}.{extension}"
                        src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
                        dst =f"{folder}/{dst}"
                        # rename all the files

                        os.rename(src, dst) 

            # Do nothing for audio files  
            else: 
                pass
            

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()

