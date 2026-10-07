# rosawolken – Command Cheat Sheet

A quick reference for the commands used to manage and access the Raspberry Pi server.

> **Legend**
>
> * **Laptop** — run the command on the development laptop
> * **rosawolken** — run the command after connecting to the Raspberry Pi via SSH

---

## 1. Connect to rosawolken

### Preferred: hostname

**Laptop**

```bash
ssh admin@rosawolken.local
```

### Fallback: IP address

If `rosawolken.local` cannot be resolved, find the Raspberry Pi's current IP address:

**rosawolken**

```bash
hostname -I
```

Then connect from the laptop:

**Laptop**

```bash
ssh admin@<IP_ADDRESS>
```

Example:

```bash
ssh admin@192.168.178.133
```

> **Note:** The IP address may change because it is assigned by DHCP. Do not assume that the example address will remain the same.

---

## 2. Find rosawolken on the local network

If the hostname does not work and you do not know the Raspberry Pi's IP address:

**Laptop**

```bash
sudo nmap -sn 192.168.178.0/24
```

Look for a device identified as **Raspberry Pi Trading**.

Use the corresponding IP address for SSH:

```bash
ssh admin@<IP_ADDRESS>
```

> The network range (`192.168.178.0/24`) depends on the local network and may need to be adjusted.

---

## 3. Verify that you are connected to rosawolken

**rosawolken**

Check the hostname:

```bash
hostname
```

Expected:

```text
rosawolken
```

Check the current IP address:

```bash
hostname -I
```

---

## 4. Leave the SSH session

**rosawolken**

```bash
exit
```

This returns to the terminal on the laptop.

---

## 5. Test network connectivity

**Laptop**

```bash
ping -c 3 rosawolken.local
```

If this succeeds, the Raspberry Pi is reachable through its hostname:)

---

## 6. Check the hostname / mDNS service

The `.local` hostname is provided through mDNS, typically using Avahi.

**rosawolken**

Check the Avahi service:

```bash
systemctl status avahi-daemon
```

Enable and start it if necessary:

```bash
sudo systemctl enable --now avahi-daemon
```

---

## 7. Update the Raspberry Pi

**rosawolken**

Update the package lists:

```bash
sudo apt update
```

Install available updates:

```bash
sudo apt upgrade
```

Or run both sequentially:

```bash
sudo apt update && sudo apt upgrade
```

---

## 8. Check a system service

**rosawolken**

```bash
systemctl status <service>
```

Example:

```bash
systemctl status avahi-daemon
```

Restart a service:

```bash
sudo systemctl restart <service>
```

Enable a service at boot:

```bash
sudo systemctl enable <service>
```

Enable and start a service immediately:

```bash
sudo systemctl enable --now <service>
```

---

## 9. View service logs

**rosawolken**

```bash
journalctl -u <service>
```

Show only recent logs:

```bash
journalctl -u <service> -n 50
```

Follow new log entries in real time:

```bash
journalctl -u <service> -f
```

---

## 10. SSH host key changed

If the Raspberry Pi is reinstalled, its SSH host key changes. The laptop may then show:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

If the change is expected (e.g. after reinstalling rosawolken), remove the old key:

**Laptop**

```bash
ssh-keygen -R <IP_ADDRESS>
```

Example:

```bash
ssh-keygen -R 192.168.178.133
```

Then reconnect:

```bash
ssh admin@<IP_ADDRESS>
```

> **Security note:** Never ignore this warning blindly. Only remove the old key when you know why the host key changed (for example, because the Raspberry Pi was reinstalled)!

---

## 11. Useful system information

**rosawolken**

Operating system information:

```bash
cat /etc/os-release
```

Kernel information:

```bash
uname -a
```

Disk usage:

```bash
df -h
```

Memory usage:

```bash
free -h
```

Current system uptime:

```bash
uptime
```

---

## Notes

* The Raspberry Pi is currently intended to be accessible **only within the local network**
* SSH is the primary method for administering rosawolken
* `rosawolken.local` is preferred over using the IP address directly
* The IP address is assigned via DHCP and may change
* Never commit passwords, SSH private keys, family photos, databases, or other secrets to the Git repository
