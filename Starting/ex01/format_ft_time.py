from datetime import datetime

epoch_time = datetime.now().timestamp()
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} \
    in scientific notation")
now = datetime.now().strftime("%b %d %Y")

print(now)
