import paramiko
# send and pull info from ssh host
# paramiko has sshclient


def connection():

    user_ip = input("enter ip: ")
    user_hostname = input("enter hostname: ")
    user_password = input("enter password: ")
    user_command = input("enter command: ")
    # user_ip=input("put down ip: ")

    # loads users host keys, ssh sha256 and so on
    client = paramiko.SSHClient()

    # for unknown/missing hosts add policy
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=user_ip, username=user_hostname,
                   password=user_password)

    stdin, stdout, stderr = client.exec_command(user_command)

    output = stdout.read().splitlines()
    for line in output:
        print(line.decode())  # print read and decoded to utf8

    client.close()  # closes ssh connection


if __name__ == '__main__':
    connection()
