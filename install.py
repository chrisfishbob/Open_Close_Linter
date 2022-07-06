import os

def main():
    os.system("sudo cp ocl.py /usr/local/bin/ocl")
    os.system("sudo chmod +x /usr/local/bin/ocl")
    print("Installation complete")

if __name__ == "__main__":
    main()
