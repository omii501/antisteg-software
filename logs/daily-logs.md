## 29/12/2025
- installed python stegano library to generated controlled steganography images for safe and responsible testing.
-created file structure for the project to maintain accountablity and handle complexity.

-worked on entropy.py and its working but there's a issue i figured out:
 -my clean image is jpeg which makes it compressed so the pixels and bits are already high in entropy 
 -the solution isn't to just change the file format to jpg,png or anyother cause my main focus was whatsapp image and the images sent on whatsapp are jpeg (compressed) so need to work on jpeg image.
 -currently the entropy seems to work but it single handendly can't prove that the image contains some hidden message so my next step would be the next detector i.e lsb_detector.py.

## 30/12/2025

-Today I worked on LSB detection.
I tested LSB statistics on a clean JPEG image and a stego image.
-Result:
- Clean image had almost equal number of 0s and 1s in LSBs
- Stego image also had near equal values but slightly shifted

At first this was confusing because I expected stego to be more random.
Then I understood:
JPEG images are already compressed, so their LSBs are already random.
Adding hidden data can actually reduce randomness instead of increasing it.
Next step:
Learn a better way (chi-square test) to measure how different the LSB pattern is.

--------------------------------------------------------------------------------------

Today I tested chi-square on JPEG images.

I found that both clean and stego images gave very distinct values which clearly showed that there is something hidden in the stego image.
Chi-square test worked extremely great and is so efficient that it worked on a jpeg image

i also found out that the analyzer which are depended on lsb detection won't efficiently work on a jpeg image cause jpeg images are already compressed so there lsbs are also randomized which wont give different value than a stego image. 
on the other hand chi-square test gave the values very distinct which clearly shows presence of a hidden message in the image(jpeg).
Clean Image Chi-Square: 0.06591726105563481
Stego Image Chi-Square: 4091.3285861467743

-----------------------------------------------------------------------------------------

Today i worked on histogram.py 
Histogram is a method which shows how often each pixel value appears in an image.
I worked on the comparison between histogram of clean img and stego img. 
-expectations: if there's difference then the stego image contains hidden message.
-expectations were true the histogram diff was very big, clearly indicating a hidden image in stego img.

i also realized that this method can be only used to dev/testing now in actual software cause the users will upload only a single image and all analysis would be on that image so no difference can be calculated.

-----------------------------------------------------------------------------------------

Today also worked on signature_scan.py

signature scan is most important and can single handedly detect(in some cases) if there's some hidden message.
signature scan scans the data and raw bytes inside the img and looks for some particular keywords like stego, stegano etc, and also looks for any executatble files, and also checks for any ASCII readable chars if there's readable chars then it return "high readable content detected" 

Analysis : when our stego img is scanned through signature scan the output appeared to be:
Signature scan findings:
- Found steganography keyword: lsb
- Embedded file signature detected: Windows executable
- Unusually high readable text content inside binary file

which clearly shows lsb keyword is used, windows.exe file is present and even high readable text content is present which clearly shows that the stego img contains some hidden data.

------------------------------------------------------------------------------------------

With signature scan we completed every analysers needed for detection: 
entropy,lsb detector, chi square test, histogram and signature scan.

## 31/12/2025

Today i worked on decision_engine.py

It helps the program decides if the risks are high by checking every analyzer's input and also gives reason for its decision.

Analysis:
The system correctly flagged the stego image as HIGH risk and clearly explained the reasons. This confirms the backend detection pipeline is working as intended.

Output:
Risk Level: HIGH
Risk Score: 10
Reasons:
- Strong statistical deviation detected (chi-square test).
- Suspicious signatures found inside the file.
- Histogram shows abnormal pixel distribution.
- LSB bit distribution deviates from normal behavior.

----------------------------------------------------------------------------------------------

Today i worked on main.py file. 
There by importing the results from every analysers and importing decision engine we get the final scan result.

## 1-1-26

Today i worked on CLI and by just running the file on terminal with the file path, that file gets scanned and the analysis is displayed.

-----------------------------------------------------------------------------------------

Today i also worked on GUI for the user to browse any file and get the scanned result. 
