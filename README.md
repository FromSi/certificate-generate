# Certificate Generate 
The user requests a certificate using a __JWT__ token. The token is hashed to __mb5__ and appended to the filename. If a file is found by this hash, the found file is returned. If not, a new one is generated.

Demo: [demo certificate](https://certificate-generate.fromsi.net/en/pdf/false/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZXJzb25fbmFtZSI6ItCS0LXQsdC10YAt0J_RhNC70Y_Rg9C80LXRgCDQktC70LDQtNC40YHQu9Cw0LIiLCJvcmdhbml6YXRpb25fbmFtZSI6IkdpdEh1YiIsImNlcnRpZmljYXRlX251bWJlciI6IkdIMDAwMSJ9.oS4mddLm0nPwFQAeZ1D69M4Y-cWhN876DKtoliKnbLY)

## Install
Installation will be using __docker__.

```bash
//--/ Cloning 
git clone git@github.com:FromSi/certificate-generate.git && cd certificate-generate

//--/ Install dotenv
cp .env.example .env

//--/ Run/Restart
make restart
```

## Example
To get a certificate, you need to make a __GET__ request:

`GET //<lang>/<file_format>/<save>/<jwt_token>`

* lang - language (en)
* file_format - what type of file to get (png|pdf)
* save - download (true|false)
* jwt_token - certificate data

`GET //en/pdf/false/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZXJzb25fbmFtZSI6ItCS0LXQsdC10YAt0J_RhNC70Y_Rg9C80LXRgCDQktC70LDQtNC40YHQu9Cw0LIiLCJvcmdhbml6YXRpb25fbmFtZSI6IkdpdEh1YiIsImNlcnRpZmljYXRlX251bWJlciI6IkdIMDAwMSJ9.oS4mddLm0nPwFQAeZ1D69M4Y-cWhN876DKtoliKnbLY`

JWT token can be reconfigured with https://jwt.io and secret-key `SECRET`.

## JWT токен
You can find the file `res/en.json` in the project. This is the config to generate certificate and merge with JWT.

When we read a file `res/en.json`. Attention to the name of the key `config`:

```
{
  "config": {
    "bg_path": "res/en_bg.png",
    "font": {
      "100": "res/fonts/StyreneAWeb-Thin.ttf",
      "300": "res/fonts/StyreneAWeb-Light.ttf",
      "400": "res/fonts/StyreneAWeb-Regular.ttf",
      "500": "res/fonts/StyreneAWeb-Medium.ttf",
      "700": "res/fonts/StyreneAWeb-Bold.ttf",
      "900": "res/fonts/StyreneAWeb-Black.ttf"
    }
  },
  ...
}
```

The configuration allows you to define the initial data for the project.

This is a block of text:

```
{
  ...,
  "organization_name_title": {
    "x": 1,
    "y": 1,
    "text_size": 32,
    "weight": 300,
    "text_color": "#2D309A",
    "text": "Organization",
    "dependence": "organization_name" <- will be generated if organization_name has text(jwt|static)
  },
  ...
}
```

If there is no `text` key, the `organization_name_title` key will be taken from the incoming JWT token.
