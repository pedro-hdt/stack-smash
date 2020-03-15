def pack64(n):
	s = ""
	while n:
		s += chr(n % 0x100)
		n = n / 0x100
	s = s.ljust(8, "\x00")
	return s




with open("exploit", "wb") as f:
    f.write(payload)

