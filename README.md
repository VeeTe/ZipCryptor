# ZipCryptor
Encrypt/Decrypt zips &amp; encapsulate 'em in one another (Python3, Linux only)


MAKE SURE THIS PROJECT HAS ITS OWN FOLDER, the functions refer to local files, thus make sure that once the source code files are downloaded they're placed in their own folder (just 1 for all sourcecode without any other unnecessary files)


If you want the keys to be created for you:
First use: GENERATEmain_keys.py
Then use: GENERATEkeys.py

If you wish to use your own keys:
delete the old keys (if exists), 
then create a keys file with passwords listed 1 per line

Once the keys are generated (either manually or automatically) you can now encrypt a file:
Open Encrypt.py and modify the 1.txt value to the name of the file you wish to encrypt
Then run the Encrypt.py

To decrypt a file make sure that the keys file is present
Make sure that the zip you wish to decrypt is in the same foulder as Decrypt.py
DECRYPT.PY IN THE END WILL DELETE ALL ZIPS IN THE SAME FOLDER AS DECRYPT.PY, SO MAKE SURE IT IS IN ITS OWN FOLDER. THIS WILL HAPPEN EVEN IF DECRYPTION IS UNSUCCESSFUL.
