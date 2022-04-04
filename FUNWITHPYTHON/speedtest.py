from turtle import speed

from stem import DownloadFailed
import speedtest
st = speedtest.speedtest()
option = int(input("""what is your internet Speed: 
1) Download speed
2) Upload speed
3) ping """))

if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames=[]
    st.get_servers(servernames)
    print(st.results.ping)       
else:
    print("Enter your Option: ")
