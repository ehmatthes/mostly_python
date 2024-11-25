from pathlib import Path
import httpx

url = "https://www.zillow.com/homedetails/"
url += "432-Park-Ave-PENTHOUSE-New-York-NY-10022/2069500049_zpid/"
r = httpx.get(url)

path = Path(__file__).parent / "output_file.html"
path.write_text(r.text)
