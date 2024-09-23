from datetime import datetime

epoch = datetime.now().timestamp()
print(f"Seconds since January 1, 1970: {epoch:,.4f} \
      or {epoch:.2e} in scientific notation")
now = datetime.now().strftime("%b %d %Y")
print(now)
