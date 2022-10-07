import os
os.mkdir('result')
if __name__ == "__main__":
        try:
                __import__("gxrex").lisensi()
        except Exception as e:
                exit(str(e))
