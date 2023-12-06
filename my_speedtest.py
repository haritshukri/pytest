import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    
    download_speed = st.download() / 1_000_000
    print(f"Download speed: {download_speed:.2f} Mbps")

    upload_speed = st.upload() / 1_000_0000
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    server = st.get_best_server()
    ping = server["latency"]
    print(f"Ping: {ping} ms")

test_internet_speed()
"""
failed because attribute error, need to learn more
"""