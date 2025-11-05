# Week 3: SSH (Secure Shell) - Beginner's Guide

SSH is a way to securely connect to other computers over the internet. Think of it like a secure telephone line to another computer.

## What You'll Learn

By the end of this lesson, you'll be able to:

- Understand what SSH is and why it's important
- Create your own SSH key (like a digital key for your house)
- Connect to a remote computer safely
- Copy files between computers securely

## What is SSH?

**SSH (Secure Shell)** is like a secure tunnel between your computer and another computer. Everything you send through this tunnel is scrambled (encrypted) so only you and the other computer can understand it.

### How SSH Works - Simple Diagram

```text
┌─────────────┐    SSH Connection    ┌─────────────┐
│   Your      │ ◄─────────────────► │   Remote    │
│  Computer   │  Encrypted Tunnel   │  Computer   │
│ (Client)    │                     │ (Server)    │
└─────────────┘                     └─────────────┘
      ↑                                     ↑
   You type                            Commands run
   commands                            safely here
```

This shows how your computer (client) connects to another computer (server) through a secure, encrypted tunnel. Everything you send is protected!

### Why Do We Need SSH?

Imagine you want to:

- Control a computer on the internet (like a web server)
- Copy files to/from that computer
- Run programs on that computer

SSH lets you do all of this **safely**. Before SSH, people used tools that sent passwords in plain text - anyone could steal them!

### Real-World Examples

- **Web developers**: Upload their websites to servers
- **System administrators**: Manage hundreds of computers remotely  
- **Students**: Access school computers from home
- **GitHub**: Upload code using SSH keys

## SSH vs Passwords: A Simple Analogy

### The Old Way (Passwords)

- Like shouting your house key number across the street
- Anyone listening can hear it
- Easy for bad guys to steal

### The SSH Way (Keys)

- Like having a special key that only fits your lock
- Even if someone sees the key, they can't copy it
- Much more secure

## Understanding SSH Keys

SSH uses two special files called keys:

### Public Key (Like a Lock)

- You can give this to anyone
- Goes on computers you want to access
- File ends with `.pub`
- Safe to share

### Private Key (Like Your House Key)

- Keep this secret! Never share it
- Stays only on your computer
- Unlocks the public key
- Very important to protect

> TL;DR: Encryption using the public key can only be reversed by the corresponding private key.
Decryption using the private key can only open something locked by its corresponding public key.

## Your First SSH Key (Step by Step)

Let's create your first SSH key together.

### Step 1: Open Your Terminal

- **Mac**: Press `Cmd + Space`, type "Terminal", press Enter
- **Windows**: Open "Command Prompt" or "PowerShell"  
- **Linux**: Press `Ctrl + Alt + T`

### Step 2: Create Your SSH Key

Type this command exactly (replace the email with yours):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Step 3: Choose Where to Save It

You'll see:

```text
Enter file in which to save the key (/Users/yourname/.ssh/id_ed25519):
```

Just press **Enter** to use the default location.

### Step 4: Create a Password (Passphrase)

You'll see:

```text
Enter passphrase (empty for no passphrase):
```

Type a password you'll remember (you won't see it as you type). Press Enter.
Then type the same password again when asked.

### Step 5: Success

You should see something like:

```text
Your identification has been saved in /Users/yourname/.ssh/id_ed25519
Your public key has been saved in /Users/yourname/.ssh/id_ed25519.pub
```

Congratulations! You now have SSH keys.

## How to Connect to Another Computer

### Basic Connection

To connect to another computer, use this format:

```bash
ssh username@computer-address
```

**Example:**

```bash
ssh john@192.168.1.100
```

This means: "Connect as user 'john' to the computer at address '192.168.1.100'"

### What Happens When You Connect

1. Your computer asks the other computer: "Can I connect?"
2. The other computer asks: "Who are you?"  
3. You prove who you are (with your key or password)
4. If accepted, you can control the other computer!

### When You're Connected

- You can type commands like you're sitting at that computer
- Type `exit` or press `Ctrl+D` to disconnect
- Everything you do is secure and encrypted

## Copying Files Between Computers

SSH lets you copy files safely between computers.

### Copy a File TO Another Computer

```bash
scp myfile.txt username@computer-address:~/
```

**Example:**

```bash
scp report.pdf john@192.168.1.100:~/Documents/
```

This copies `report.pdf` from your computer to John's Documents folder.

### Copy a File FROM Another Computer  

```bash
scp username@computer-address:~/filename.txt ~/Downloads/
```

**Example:**

```bash
scp john@192.168.1.100:~/photos.zip ~/Downloads/
```

This copies `photos.zip` from John's computer to your Downloads folder.

## Practice Exercises

### Exercise 1: Create Your SSH Key

1. Open your terminal
2. Run: `ssh-keygen -t ed25519 -C "your-email@example.com"`
3. Press Enter for default location
4. Enter a passphrase you'll remember
5. Check if it worked: `ls ~/.ssh/`

You should see two files:

- `id_ed25519` (your private key - keep secret!)
- `id_ed25519.pub` (your public key - safe to share)

### Exercise 2: Look at Your Public Key

Run this command:

```bash
cat ~/.ssh/id_ed25519.pub
```

You'll see a long line of random characters. This is your public key!

### Exercise 3: Practice SCP (If You Have Two Computers)

1. Create a test file: `echo "Hello SSH!" > test.txt`
2. Copy it to another computer: `scp test.txt user@other-computer:~/`
3. Connect to the other computer and check if the file is there

## SSH Safety Rules

### ✅ DO

- Keep your private key secret (the file without .pub)
- Use strong passphrases
- Share your public key (.pub file) when needed  
- Log out when you're done: type `exit`
- Only connect to computers you trust

### ❌ DON'T

- Share your private key (file without .pub)
- Use the same password everywhere
- Leave SSH connections open
- Connect to computers you don't trust
- Give your private key to anyone

## Common Beginner Mistakes

### Mistake 1: "Permission denied"

**Problem:** Your key isn't set up on the other computer  
**Solution:** Ask the computer owner to add your public key

### Mistake 2: "Connection refused"

**Problem:** The other computer isn't accepting SSH connections  
**Solution:** Ask the computer owner to enable SSH

### Mistake 3: "Host key verification failed"

**Problem:** The computer's identity changed  
**Solution:** Ask an expert - this could be a security issue!

### Mistake 4: Wrong File Permissions

**Problem:** SSH complains about file permissions  
**Solution:** Run these commands:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

## What You've Learned

- ✅ SSH is like a secure telephone line to other computers
- ✅ SSH keys are like digital house keys (safer than passwords)  
- ✅ You have a public key (safe to share) and private key (keep secret)
- ✅ You can control other computers with `ssh username@address`
- ✅ You can copy files with `scp filename username@address:~/`
- ✅ Always follow SSH safety rules

## What's Next?

Once you're comfortable with these basics:

1. **Practice with a friend** - Try connecting to each other's computers
2. **Learn SSH config files** - Make connections easier
3. **Try cloud servers** - Practice with AWS, DigitalOcean, etc.
4. **Explore GitHub** - Use SSH keys for code management

## Quick Reference

### Essential Commands

```bash
# Create SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Connect to computer
ssh username@computer-address

# Copy file TO computer
scp file.txt username@computer-address:~/

# Copy file FROM computer  
scp username@computer-address:~/file.txt ~/Downloads/

# Exit SSH connection
exit
```

### File Locations

- Your private key: `~/.ssh/id_ed25519`
- Your public key: `~/.ssh/id_ed25519.pub`
- SSH config: `~/.ssh/config`

Remember: SSH is powerful but safe when you follow the rules. Start simple and practice!

## Key Types Comparison

| Type | Security | Compatibility | Key Size | Recommended |
|------|----------|---------------|----------|-------------|
| **Ed25519** | Excellent | Good (newer systems) | Small | ✅ Yes (new keys) |
| **RSA 4096** | Excellent | Excellent | Large | ✅ Yes (legacy compatibility) |
| **RSA 2048** | Good | Excellent | Medium | ⚠️ Minimum acceptable |
| **ECDSA** | Good | Good | Medium | ❌ Not recommended |
| **DSA** | Poor | Legacy only | Small | ❌ Deprecated |

## Installing Public Keys on Remote Servers

### Method 1: Using ssh-copy-id (Easiest)

```bash
# Copy your public key to the remote server
ssh-copy-id username@hostname

# Or specify a specific key
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@hostname
```

### Method 2: Manual Copy

```bash
# 1. Copy your public key content
cat ~/.ssh/id_ed25519.pub

# 2. Log into the remote server
ssh username@hostname

# 3. Create .ssh directory (if it doesn't exist)
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 4. Add your public key to authorized_keys
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5... your_email@example.com" >> ~/.ssh/authorized_keys

# 5. Set correct permissions
chmod 600 ~/.ssh/authorized_keys
```

### Method 3: Using Cloud Provider Interfaces

Most cloud providers (AWS, DigitalOcean, etc.) allow you to add SSH keys through their web interfaces when creating instances.

## Basic SSH Commands

### Connecting to Remote Servers

```bash
# Basic connection
ssh username@hostname

# Specify port (default is 22)
ssh -p 2222 username@hostname

# Use specific key
ssh -i ~/.ssh/my_key username@hostname

# Enable verbose output (for debugging)
ssh -v username@hostname

# Run a single command and exit
ssh username@hostname "ls -la /var/log"
```

### Common SSH Options

| Option | Description | Example |
|--------|-------------|---------|
| `-p` | Specify port | `ssh -p 2222 user@host` |
| `-i` | Use specific key | `ssh -i ~/.ssh/key user@host` |
| `-v` | Verbose output | `ssh -v user@host` |
| `-X` | Enable X11 forwarding | `ssh -X user@host` |
| `-L` | Local port forwarding | `ssh -L 8080:localhost:80 user@host` |
| `-R` | Remote port forwarding | `ssh -R 9090:localhost:3000 user@host` |
| `-N` | Don't execute remote command | `ssh -N -L 8080:db:5432 user@host` |

## SSH Configuration File

Create `~/.ssh/config` to simplify connections:

```text
# ~/.ssh/config

# Default settings for all hosts
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3

# Specific server configuration
Host myserver
    HostName 192.168.1.100
    User john
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

# GitHub configuration
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

# AWS server with bastion host
Host aws-private
    HostName 10.0.1.50
    User ec2-user
    ProxyJump bastion
    IdentityFile ~/.ssh/aws-key.pem

Host bastion
    HostName bastion.example.com
    User ubuntu
    IdentityFile ~/.ssh/bastion-key.pem
```

With this config, you can simply run:

```bash
# Instead of: ssh -p 2222 -i ~/.ssh/id_ed25519 john@192.168.1.100
ssh myserver

# Instead of: ssh -i ~/.ssh/aws-key.pem ec2-user@10.0.1.50
ssh aws-private
```

## File Transfers with SSH

### SCP (Secure Copy)

```bash
# Copy file to remote server
scp file.txt username@hostname:/path/to/destination/

# Copy file from remote server
scp username@hostname:/path/to/file.txt local-destination/

# Copy directory recursively
scp -r local-directory/ username@hostname:/remote/path/

# Use specific SSH key
scp -i ~/.ssh/id_ed25519 file.txt username@hostname:~/
```

### SFTP (SSH File Transfer Protocol)

```bash
# Start SFTP session
sftp username@hostname

# SFTP commands
sftp> ls                    # List remote files
sftp> lls                   # List local files
sftp> pwd                   # Show remote directory
sftp> lpwd                  # Show local directory
sftp> cd /path              # Change remote directory
sftp> lcd /local/path       # Change local directory
sftp> get remote_file.txt   # Download file
sftp> put local_file.txt    # Upload file
sftp> mget *.txt            # Download multiple files
sftp> mput *.txt            # Upload multiple files
sftp> quit                  # Exit SFTP
```

### rsync over SSH

For more advanced file synchronization:

```bash
# Sync directory to remote server
rsync -avz -e ssh local-dir/ username@hostname:/remote/dir/

# Sync from remote server
rsync -avz -e ssh username@hostname:/remote/dir/ local-dir/

# Exclude certain files
rsync -avz --exclude='*.log' -e ssh local-dir/ username@hostname:/remote/dir/
```

## SSH Agent and Key Management

### Starting SSH Agent

```bash
# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# List loaded keys
ssh-add -l

# Remove all keys from agent
ssh-add -D
```

### Adding to Shell Profile

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Auto-start SSH agent
if ! pgrep -u "$USER" ssh-agent > /dev/null; then
    ssh-agent -t 1h > "$XDG_RUNTIME_DIR/ssh-agent.env"
fi
if [[ ! "$SSH_AUTH_SOCK" ]]; then
    source "$XDG_RUNTIME_DIR/ssh-agent.env" >/dev/null
fi
```

## SSH Tunneling (Port Forwarding)

### Local Port Forwarding

Forward local port to remote service:

```bash
# Forward local port 8080 to remote port 80
ssh -L 8080:localhost:80 username@hostname

# Access remote database through SSH tunnel
ssh -L 5432:database-server:5432 username@gateway-server
```

Now you can access `http://localhost:8080` and it will connect to the remote server's port 80.

### Remote Port Forwarding

Forward remote port to local service:

```bash
# Forward remote port 9090 to local port 3000
ssh -R 9090:localhost:3000 username@hostname
```

### Dynamic Port Forwarding (SOCKS Proxy)

```bash
# Create SOCKS proxy on local port 1080
ssh -D 1080 username@hostname
```

## Security Best Practices

### Server-Side Security

1. **Disable password authentication** (after setting up keys):

   ```bash
   # In /etc/ssh/sshd_config
   PasswordAuthentication no
   PubkeyAuthentication yes
   ```

2. **Change default port**:

   ```bash
   # In /etc/ssh/sshd_config
   Port 2222
   ```

3. **Disable root login**:

   ```bash
   # In /etc/ssh/sshd_config
   PermitRootLogin no
   ```

4. **Use fail2ban** to prevent brute force attacks:

   ```bash
   sudo apt install fail2ban
   ```

### Client-Side Security

1. **Use passphrases on private keys**
2. **Keep private keys secure** (permissions 600)
3. **Use SSH agent** to avoid typing passphrases repeatedly
4. **Verify host keys** when connecting to new servers
5. **Use recent SSH client** software

### File Permissions

Correct SSH file permissions are crucial:

```bash
chmod 700 ~/.ssh                    # SSH directory
chmod 600 ~/.ssh/id_ed25519         # Private key
chmod 644 ~/.ssh/id_ed25519.pub     # Public key
chmod 600 ~/.ssh/authorized_keys    # Authorized keys
chmod 600 ~/.ssh/config             # SSH config
chmod 600 ~/.ssh/known_hosts        # Known hosts
```

## Troubleshooting Common Issues

### 1. Permission Denied (publickey)

**Problem**: Can't authenticate with SSH key

**Solutions**:

```bash
# Check if key is loaded in SSH agent
ssh-add -l

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Check file permissions
ls -la ~/.ssh/

# Test connection with verbose output
ssh -v username@hostname
```

### 2. Connection Refused

**Problem**: Can't connect to server

**Solutions**:

- Check if SSH service is running on server
- Verify port number (default 22)
- Check firewall settings
- Verify hostname/IP address

```bash
# Test connectivity
ping hostname
telnet hostname 22
```

### 3. Host Key Verification Failed

**Problem**: Server's host key has changed

**Solutions**:

```bash
# Remove old host key
ssh-keygen -R hostname

# Or edit known_hosts file
nano ~/.ssh/known_hosts
```

### 4. Too Many Authentication Failures

**Problem**: SSH trying too many keys

**Solutions**:

```bash
# Use specific key
ssh -o IdentitiesOnly=yes -i ~/.ssh/specific_key username@hostname

# Or limit keys in SSH config
Host hostname
    IdentitiesOnly yes
    IdentityFile ~/.ssh/specific_key
```

## Working with Different Operating Systems

### Windows

1. **Built-in SSH** (Windows 10+):

   ```cmd
   ssh username@hostname
   ```

2. **PuTTY**: Graphical SSH client
   - Generate keys with PuTTYgen
   - Convert between key formats

3. **Windows Subsystem for Linux (WSL)**:
   Full Linux SSH experience on Windows

### macOS

SSH is pre-installed:

```bash
# Same commands as Linux
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh username@hostname
```

### Linux

SSH client usually pre-installed:

```bash
# Install if missing (Ubuntu/Debian)
sudo apt update && sudo apt install openssh-client

# Install if missing (RHEL/CentOS)
sudo yum install openssh-clients
```

## Practical Exercises

### Exercise 1: Generate SSH Keys

1. Generate an Ed25519 SSH key pair
2. View your public key
3. Check file permissions

```bash
# Your commands here
ssh-keygen -t ed25519 -C "student@example.com"
cat ~/.ssh/id_ed25519.pub
ls -la ~/.ssh/
```

### Exercise 2: SSH Configuration

1. Create an SSH config file
2. Add configuration for a server
3. Test the connection

```bash
# Edit config file
nano ~/.ssh/config

# Add your server configuration
# Test connection
ssh myserver
```

### Exercise 3: File Transfer

1. Create a test file locally
2. Transfer it to a remote server using SCP
3. Verify the transfer using SSH

```bash
# Create test file
echo "Hello SSH!" > test.txt

# Transfer file
scp test.txt username@hostname:~/

# Verify on remote server
ssh username@hostname "cat test.txt"
```

## Real-World Scenarios

### Scenario 1: Connecting to Cloud Servers

```bash
# AWS EC2 instance
ssh -i ~/.ssh/aws-key.pem ec2-user@ec2-123-456-789.compute-1.amazonaws.com

# DigitalOcean droplet
ssh root@your-droplet-ip

# Google Cloud instance
gcloud compute ssh instance-name --zone=us-central1-a
```

### Scenario 2: Development Workflow

```bash
# Connect to development server
ssh dev-server

# Edit code remotely
nano /var/www/html/index.php

# Transfer updated files
scp -r local-project/ dev-server:/var/www/html/

# Restart services
ssh dev-server "sudo systemctl restart apache2"
```

### Scenario 3: Database Access Through Bastion

```bash
# SSH config for bastion host
Host bastion
    HostName bastion.company.com
    User admin

Host database
    HostName db.internal.company.com
    User dbadmin
    ProxyJump bastion

# Connect to database through bastion
ssh database

# Or create tunnel for database access
ssh -L 5432:db.internal.company.com:5432 bastion
```

## Going Further

### Advanced Topics

1. **SSH Certificates**: Alternative to key-based authentication
2. **SSH-CA**: Certificate Authority for SSH
3. **Multiplexing**: Reuse SSH connections
4. **Escape Sequences**: Control SSH sessions
5. **SFTP Servers**: Set up your own file transfer server

### Integration with Other Tools

- **Git**: SSH keys for GitHub/GitLab
- **Ansible**: SSH for automation
- **Docker**: SSH into containers
- **VS Code**: Remote development over SSH
- **tmux/screen**: Persistent sessions over SSH

## Summary

SSH is a fundamental tool for anyone working with remote systems. Key takeaways:

1. **Always use SSH keys** instead of passwords when possible
2. **Secure your private keys** with passphrases and proper permissions
3. **Use SSH config** to simplify connections
4. **Learn file transfer methods** (SCP, SFTP, rsync)
5. **Understand port forwarding** for accessing remote services
6. **Follow security best practices** on both client and server

Master SSH, and you'll have one of the most important tools in your toolkit for system administration, development, and DevOps work.

## Resources

- [OpenSSH Manual Pages](https://man.openbsd.org/ssh)
- [SSH.com SSH Academy](https://www.ssh.com/academy/ssh)
- [GitHub SSH Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [DigitalOcean SSH Tutorials](https://www.digitalocean.com/community/tutorials?q=ssh)
- [SSH Best Practices](https://blog.0xbadc0de.be/archives/300)

Happy SSH-ing! 🔐
