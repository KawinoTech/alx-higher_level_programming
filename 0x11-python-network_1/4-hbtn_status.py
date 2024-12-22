if __name__ == "__main__":
    import requests
    respon = requests.get('https://alx-intranet.hbtn.io/status')
    resp_data = respon.text
    body_type = type(resp_data)
    print(
        "Body response:\n"
        "\t- type: {}\n"
        "\t- content: {}"
        .format(body_type, resp_data)
    )
