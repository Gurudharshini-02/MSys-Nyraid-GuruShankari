import paramiko


src = 'D:/Python/file1.py'
dest= 'E:/Python_Practice'


hostname = 'CHN-REN-GURUSH'
username = 'guru'
password = 'kiruthiga'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect(hostname=hostname, username=username, password=password)


sftp = ssh.open_sftp()


sftp.get(src, dest)

sftp.close()
ssh.close()

