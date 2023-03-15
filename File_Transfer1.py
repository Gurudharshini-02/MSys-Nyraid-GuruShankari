import paramiko
import argparse


def file_transfer(hostname,username,password):
    src = '/home/ubuntu/file/sample.txt'
    dest= '/home/ubuntu'

    #Connection for SSH
    ssh = paramiko.SSHClient()
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname=hostname, username=username, password=password)

    #open secure file transfer protocol connection
    sftp = ssh.open_sftp()


    sftp.get(src, dest)

    sftp.close()
    ssh.close()

    return "File Copied"

if __name__='__main__':

    parser=argparse.ArgumentParser(description='Transfer of file from one machine to other')
    parser.add_argument('--hostname',help='hostname')
    parser.add_argument('--username',help='username')
    parser.add_argument('--password',help='password')

    args=parser.parse_args()
    file_transfer(args.hostname,args.username,args.password)
    
    

