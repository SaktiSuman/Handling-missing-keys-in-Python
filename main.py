country_code = {
    "India":'0091',
    "Pakistan":'0000',
    "China":"0089"
}
country_code.setdefault("Japan", "Not Present")
print(country_code["India"])
print(country_code["Japan"])